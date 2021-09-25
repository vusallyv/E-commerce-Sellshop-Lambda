from django.shortcuts import render

# Create your views here.

from django.db.models import Q, F
from product.models import Blog, Category, ProductVersion, Image, Review, Product, Comment, Brand

def product_list(request):
    qs_productversion_all = ProductVersion.objects.all()
    qs_product = Product.objects.all()
    qs_category = Category.objects.all()
    qs_brand = Brand.objects.all()
    qs = None
    if request.POST.get("search_name"):
        qs = ProductVersion.objects.filter( Q(product_id__title__icontains=request.POST.get("search_name")) | Q(product_id__subtitle__icontains=request.POST.get("search_name")) | Q(product_id__description__icontains=request.POST.get("search_name")) )
    
    if request.POST.get("category_name"):
        qs_productversion_all = ProductVersion.objects.filter( product_id__category__title=request.POST.get("category_name"))

    if request.POST.get("subcategory_name"):
        qs_productversion_all = ProductVersion.objects.filter( product_id__category__subcategories__title=request.POST.get("subcategory_name"))
    context = {
        'title': 'Product-list Sellshop',
        'productversions': qs,
        'brands': qs_brand,
        'allproductversions': qs_productversion_all[0:8],
        'products': qs_product,
        'categories': qs_category
    }
    return render(request, 'product-list.html', context=context)

def single_blog(request):
    qs = Blog.objects.order_by('-created_at')
    qs_comment = Comment.objects.all()

    context = {
        'title': 'Single-blog Sellshop',
        'blogs': qs[0:3],
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
    return render(request, 'single-product.html',context=context)

