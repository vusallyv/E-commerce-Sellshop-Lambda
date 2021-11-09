from django.shortcuts import render
from blog.models import Blog, Comment
from product.models import Brand, Category
from django.views.generic import DetailView, ListView
from blog.forms import CommentForm


def single_blog(request, pk):
    qs_one_blog = Blog.objects.get(pk=pk)
    qs_blogs = Blog.objects.order_by('-created_at').exclude(id=pk)
    qs_category = Category.objects.all()
    qs_comment = Comment.objects.filter(blog=pk)
    qs_brand = Brand.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                description=request.POST.get('description'),
                blog=Blog.objects.get(pk=pk),
                user=request.user
            )
            comment.save()
    else:
        form = CommentForm()

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
        # context['brands'] = Brand.objects.all()
        context['blogs'] = Blog.objects.order_by(
            '-created_at').exclude(pk=self.kwargs.get('pk'))
        context['form'] = CommentForm
        # context['categories'] = Category.objects.all()
        context['title'] = 'Single-blog Sellshop'
        return context


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'

    def get_blogs(self):
        qs = Blog.objects.all()[0:3]
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog-list Sellshop'
        context['blogs'] = self.get_blogs()
        return context
