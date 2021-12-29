from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Project
from .forms import ProductForm


def all_products(request):
    """ A view to show each product details """

    products = Product.objects.all()
    query = None
    projects = None

    if request.GET:
        if 'project' in request.GET:
            projects = request.GET['project'].split(',')
            products = products.filter(project__name__in=projects)
            projects = Project.objects.filter(name__in=projects)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term' : query,
        'current_projects': projects,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show all products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
    