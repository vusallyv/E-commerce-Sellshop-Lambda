from django.shortcuts import render

# Create your views here.

from django.db.models import Q, F
from product.models import Blog, Category, Color, ProductVersion, Image, Review, Product, Comment, Brand, Size


def product_list(request):
    qs_productversion_all = ProductVersion.objects.all()
    qs_productversion_best = ProductVersion.objects.order_by('-rating')[0]
    qs_product = Product.objects.all()
    qs_category = Category.objects.all()
    qs_brand = Brand.objects.all()
    qs = None
    qs_color = Color.objects.all()
    qs_size = Size.objects.all()

    if request.POST.get("search_name"):
        qs = ProductVersion.objects.filter(Q(product__title__icontains=request.POST.get("search_name")) | Q(
            product__subtitle__icontains=request.POST.get("search_name")) | Q(product__description__icontains=request.POST.get("search_name")))
    elif request.POST.get("category_name"):
        qs_productversion_all = ProductVersion.objects.filter(
            product__category__title=request.POST.get("category_name"))
    elif request.POST.get("subcategory_name"):
        qs_productversion_all = ProductVersion.objects.filter(
            product__category__subcategories__title=request.POST.get("subcategory_name"))
    elif request.POST.get("size"):
        qs_productversion_all = ProductVersion.objects.filter(
            size__title=request.POST.get("size"))
    elif request.POST.get("brand"):
        qs_productversion_all = ProductVersion.objects.filter(
            product__brand__title=request.POST.get("brand"))

    context = {
        'title': 'Product-list Sellshop',
        'productversions': qs,
        'brands': qs_brand,
        'allproductversions': qs_productversion_all[0:8],
        'bestproductversion': qs_productversion_best,        
        'products': qs_product,
        'categories': qs_category,
        'sizes': qs_size

    }
    return render(request, 'product-list.html', context=context)


def single_blog(request):
    qs = Blog.objects.order_by('-created_at')
    qs_category = Category.objects.all()
    qs_comment = Comment.objects.all()
    qs_brand = Brand.objects.all()


    context = {
        'title': 'Single-blog Sellshop',
        'blogs': qs[0:3],
        'relatedblogs': qs[1::],
        'categories': qs_category,
        'brands': qs_brand,
        'comments': qs_comment,
    }
    return render(request, 'single-blog.html', context=context)


def single_product(request):
    qs_productversion_all = ProductVersion.objects.all()
    qs_reviews = Review.objects.all()
    context = {
        'title': 'Single-product Sellshop',
        'allproductversions': qs_productversion_all[0],
        'reviews': qs_reviews,
    }
    return render(request, 'single-product.html', context=context)
