from django.shortcuts import render

from product.models import Category, Subcategory
from product.models import ProductVersion, Product, Image

from django.db.models import Q


def single_blog(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {
        'title': 'Single-blog Sellshop',
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'single-blog.html', context=context)


def single_product(request):
    # qs_image = Image.objects.all()
    qs = ProductVersion.objects.all()[0:1]
   
    context = {
        'title': 'Single-product Sellshop',
        'products': qs,
        # 'images': qs_image,
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
