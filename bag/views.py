from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag content page """

    return render(request, 'bag/bag.html')


# Views by The Code Institute, Boutique Ado project. Thanks
# Add To The Bag View
def add_to_bag(request, item_id):
    """ Add a quantity of the specific product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    frame = None
    if 'product_frame' in request.POST:
        frame = request.POST['product_frame']
    bag = request.session.get('bag', {})

    if frame:
        if item_id in list(bag.keys()):
            if frame in bag[item_id]['items_by_frame'].keys():
                bag[item_id]['items_by_frame'][frame] += quantity
                messages.success(
                    request, f'Added {product.name} {frame.upper()} frame')
            else:
                bag[item_id]['items_by_frame'][frame] = quantity
                messages.success(
                    request, f'{product.name} {frame.upper()} frame added')
        else:
            bag[item_id] = {'items_by_frame': {frame: quantity}}
            messages.success(
                request,
                f'{product.name} with {frame.upper()} frame is in the Bag!')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to the Shopping Bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)

# Adjust The Bag View


def adjust_bag(request, item_id):
    """ Adjust a quantity of products in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    frame = None
    if 'product_frame' in request.POST:
        frame = request.POST['product_frame']
    bag = request.session.get('bag', {})

    if frame:
        if quantity > 0:
            bag[item_id]['items_by_frame'][frame] = quantity
            messages.success(
                request,
                f'Updated the quantity of {product.name}')
        else:
            del bag[item_id]['items_by_frame'][frame]
            if not bag[item_id]['items_by_frame']:
                bag.pop(item_id)
            messages.success(
                request,
                f'{product.name} with {frame.upper()} frame now removed!')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'{product.name} removed from the Shopping Bag!')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

# Remove From The Bag View


def remove_from_bag(request, item_id):
    """ Removes the item from the shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        frame = None
        if 'product_frame' in request.POST:
            frame = request.POST['product_frame']
        bag = request.session.get('bag', {})

        if frame:
            del bag[item_id]['items_by_frame'][frame]
            if not bag[item_id]['items_by_frame']:
                bag.pop(item_id)
            messages.success(
                request,
                f'{product.name} with {frame.upper()} frame has been removed')
        else:
            bag.pop(item_id)
            messages.success(
                request, f'Removed {product.name} from the Shopping Bag!')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
