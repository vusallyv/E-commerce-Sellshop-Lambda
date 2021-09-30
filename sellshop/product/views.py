from django.shortcuts import render

# Create your views here.

from django.db.models import Q, F
from product.models import Blog, Category, Color, ProductVersion, Image, Review, Product, Comment, Brand, Size
from account.models import User
from product.forms import CommentForm


def product_list(request):
    qs_productversion_all = ProductVersion.objects.all()
    qs_productversion_best = ProductVersion.objects.order_by('-rating')[0]
    qs_product = Product.objects.all()
    qs_brand = Brand.objects.all()
    qs = None
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
        'sizes': qs_size,
        'bestproductversion': qs_productversion_best,
        'products': qs_product,
    }
    return render(request, 'product-list.html', context=context)


def single_blog(request, pk):
    qs_one_blog = Blog.objects.get(pk=pk)
    qs_blogs = Blog.objects.order_by('-created_at').exclude(id=pk)
    qs_category = Category.objects.all()
    qs_comment = Comment.objects.filter(blog_id=pk)
    qs_brand = Brand.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()

    context = {
        'title': 'Single-blog Sellshop',
        'blogs': qs_blogs[0:3],
        'relatedblogs': qs_blogs,
        'firstblog': qs_one_blog,
        'categories': qs_category,
        'brands': qs_brand,
        'comments': qs_comment,
        'form': CommentForm,
    }
    return render(request, 'single-blog.html', context=context)


def single_product(request, pk):
    qs_productversion_all = ProductVersion.objects.get(pk=pk)
    qs_reviews = Review.objects.all()
    context = {
        'title': 'Single-product Sellshop',
        'allproductversions': qs_productversion_all,
        'reviews': qs_reviews,
    }
    return render(request, 'single-product.html', context=context)
