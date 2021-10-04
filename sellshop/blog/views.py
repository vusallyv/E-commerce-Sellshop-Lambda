from django.shortcuts import render
from blog.models import Blog
from django.db.models import Q
from product.models import Category, Subcategory, Product
from django.views.generic import ListView


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


def single_blog(request, pk):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    blog_id = Blog.objects.get(pk=pk)
    all_blogs = Blog.objects.all()[0:3]
    # one_blog = Blog.objects.get(pk=pk)
    context = {
        'title': 'Single-blog Sellshop',
        'categories': categories,
        'subcategories': subcategories,
        'blog_id': blog_id,
        'all_blogs': all_blogs,
        # 'one_blog': one_blog,
    }
    return render(request, 'single-blog.html', context=context)


class Bloglist(ListView):
    model = Blog
    # context_object_name = 'blogs'
    template_name = 'blog.html'

    def get_blogs(self):
        qs = Blog.objects.all()[0:3]
        return qs
    
    # def get_comments(self):
    #     qs = Comment.objects.all()[0:3]
    #     return qs
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = self.get_blogs()
        # context['comments'] = self.get_comments()
        return context
