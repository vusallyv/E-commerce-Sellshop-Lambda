from django.shortcuts import render

# Create your views here.

from product.models import Product

def about(request):
    context = {
        'title': 'About Sellshop',
    }
    return render(request, 'about.html', context=context)

def blog(request):
    context = {
        'title': 'Blog Sellshop',
    }
    return render(request, 'blog.html', context=context)

def error_404(request):
    context = {
        'title': 'Error Sellshop',
    }
    return render(request, 'error-404.html', context=context)

def index(request):
    context = {
        'title': 'Home Sellshop',
    }
    return render(request, 'index.html', context=context)
