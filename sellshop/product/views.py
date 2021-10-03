from django.shortcuts import render

from django.views.generic import View
from product.models import Category, Subcategory, Product, Image, ProductVersion, Tag
from django.db.models import Q
from product.forms import ReviewForm


def single_product(request, pk):
    image = Image.objects.get(pk=pk)
    product = Product.objects.get(pk=pk)
    product_versions = ProductVersion.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
   
    context = {
        'title': 'Single-product Sellshop',
        'images': image,
        'product': product,
        'form': ReviewForm(),
        'product_versions': product_versions
    }
    return render(request, 'single-product.html', context=context)



def product_list(request):
    products = Product.objects.order_by('price')[0:4]
    images = Image.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    
    context = {
        'title': 'Product-list Sellshop',
        'products': products,
        'images': images,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'product-list.html', context=context)

