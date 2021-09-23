from django.shortcuts import render

# Create your views here.

def product_list(request):
    context = {
        'title': 'Product-list Sellshop'
    }
    return render(request, 'product-list.html', context=context)

def single_blog(request):
    context = {
        'title': 'Single-blog Sellshop'
    }
    return render(request, 'single-blog.html', context=context)

def single_product(request):
    context = {
        'title': 'Single-product Sellshop'
    }
    return render(request, 'single-product.html',context=context)

