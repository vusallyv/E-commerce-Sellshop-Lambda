from django.shortcuts import render
from product.models import Blog
from django.db.models import Q
# Create your views here.



def about(request):
    context = {
        'title': 'About Sellshop',
    }
    return render(request, 'about.html', context=context)


def blog(request):
    all_blog = None
    if request.POST.get("search_name"):
        all_blog = Blog.objects.filter(
            Q(title__icontains=request.POST.get("search_name")) | Q(description__icontains=request.POST.get("search_name"))
        )[0:9]
    # all_blog = Blog.objects.all()[0:9]
    context = {
        'title': 'Blog Sellshop',
        'all_blog': all_blog,
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


