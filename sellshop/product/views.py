from django.shortcuts import render

# Create your views here.

from django.db.models import Q
from product.models import Blog, ProductVersion, Image, Review, Product, Comment

def product_list(request):
    qs_productversion_all = ProductVersion.objects.all()
    # qs_image = Image.objects.all()
    qs_product = Product.objects.all()
    qs = None
    if request.POST.get("search_name"):
        qs = ProductVersion.objects.filter( Q(product_id__title__icontains=request.POST.get("search_name")) | Q(product_id__subtitle__icontains=request.POST.get("search_name")) | Q(product_id__description__icontains=request.POST.get("search_name")) )
    
    if request.POST.get("category_name"):
        qs_productversion_all = ProductVersion.objects.filter( product_id__category_id__title=request.POST.get("category_name"))
    context = {
        'title': 'Product-list Sellshop',
        'productversions': qs,
        # 'images': qs_image,
        'allproductversions': qs_productversion_all[0:8],
        'products': qs_product,
    }
    return render(request, 'product-list.html', context=context)

def single_blog(request):
    qs = Blog.objects.order_by('-created_at')
    qs_comment = Comment.objects.filter(blog_id=1)

    context = {
        'title': 'Single-blog Sellshop',
        'blogs': qs[0:3],
        'comments': qs_comment,
    }
    return render(request, 'single-blog.html', context=context)

def single_product(request):
    qs_productversion_all = ProductVersion.objects.all()
    qs_reviews = Review.objects.filter(product_id=1)
    context = {
        'title': 'Single-product Sellshop',
        'allproductversions': qs_productversion_all[0],
        'reviews': qs_reviews,
    }
    return render(request, 'single-product.html',context=context)

