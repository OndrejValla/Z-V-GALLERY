from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag content page """

    return render(request, 'bag/bag.html')

# Views by Code Institute, Boutique project. Thanks
def add_to_bag(request, item_id):
    """ Add a quantity of the specific product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    frame = None
    if 'product_frame' in request.POST:
        frame = request.POST['product_frame']
    bag = request.session.get('bag', {})
    messages.success(request, f'Updated frame selection')
    if frame:
        if item_id in list(bag.keys()):
            if frame in bag[item_id]['items_by_frame'].keys():
                bag[item_id]['items_by_frame'][frame] += quantity

            else:
                bag[item_id]['items_by_frame'][frame] = quantity
        else:
            bag[item_id] = {'items_by_frame': {frame: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to the Shopping Bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust a quantity of products in the shopping bag """

    quantity = int(request.POST.get('quantity'))
    frame = None
    if 'product_frame' in request.POST:
        frame = request.POST['product_frame']
    bag = request.session.get('bag', {})

    if frame:
        if quantity > 0:
            bag[item_id]['items_by_frame'][frame] = quantity
        else:
            del bag[item_id]['items_by_frame'][frame]
            if not bag[item_id]['items_by_frame']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Removes the item from the shopping bag """

    try:
        frame = None
        if 'product_frame' in request.POST:
            frame = request.POST['product_frame']
        bag = request.session.get('bag', {})

        if frame:
            del bag[item_id]['items_by_frame'][frame]
            if not bag[item_id]['items_by_frame']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
