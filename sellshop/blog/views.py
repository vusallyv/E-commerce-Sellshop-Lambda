from django.shortcuts import render
from blog.models import Blog, Comment
from product.models import Brand, Category
from django.views.generic import DetailView, ListView
from blog.forms import CommentForm
from django.core.paginator import Paginator


def single_blog(request, pk):
    qs_one_blog = Blog.objects.get(pk=pk)
    qs_blogs = Blog.objects.order_by('-created_at').exclude(id=pk)
    qs_category = Category.objects.all()
    qs_comment = Comment.objects.filter(blog=pk)
    qs_brand = Brand.objects.all()

    context = {
        'title': 'Single-blog Sellshop',
        'blogs': qs_blogs[0:3],
        'relatedblogs': qs_blogs,
        'blog': qs_one_blog,
        'categories': qs_category,
        'brands': qs_brand,
        'comments': qs_comment,
        'form': CommentForm,
    }
    return render(request, 'single-blog.html', context=context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'single-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.order_by(
            '-created_at').exclude(pk=self.kwargs.get('pk'))[0:5]
        context['form'] = CommentForm
        context['title'] = 'Single-blog Sellshop'
        return context


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'

    def get_blogs(self):
        qs = Blog.objects.all()[0:6]
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog-list Sellshop'
        context['blogs'] = self.get_blogs()
        return context


def BlogList(request):
    blog_list = Blog.objects.order_by('-created_at')
    paginator = Paginator(blog_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Blog-list Sellshop',
        'page_obj': page_obj,
    }
    return render(request, 'blog.html', context=context)
