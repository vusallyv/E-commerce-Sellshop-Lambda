from django.shortcuts import render

# Create your views here.

def product_list(request):
    return render(request, 'product-list.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def single_product(request):
    return render(request, 'single-product.html')

