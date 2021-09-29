from django.shortcuts import render
from blog.models import Blog
from django.db.models import Q
from product.models import Category, Subcategory, Product


def blog(request):
    # all_blog = None
    # if request.POST.get("search_name"):
    #     all_blog = Blog.objects.filter(
    #         Q(title__icontains=request.POST.get("search_name")) | Q(
    #             description__icontains=request.POST.get("search_name"))
    #     )[0:9]
    all_blog = Blog.objects.all()[0:3]
    
    context = {
        'title': 'Blog Sellshop',
        'all_blog': all_blog,
        
    }
    return render(request, 'blog.html', context=context)


def single_blog(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    all_blogs2 = Blog.objects.all()[0:1]
    all_blogs = Blog.objects.all()[0:3]
    # one_blog = Blog.objects.get(pk=pk)
    context = {
        'title': 'Single-blog Sellshop',
        'categories': categories,
        'subcategories': subcategories,
        'all_blogs2': all_blogs2,
        'all_blogs': all_blogs,
        # 'one_blog': one_blog, 
    }
    return render(request, 'single-blog.html', context=context)

