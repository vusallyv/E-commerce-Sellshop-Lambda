from django.shortcuts import render
from django.views.generic.edit import FormMixin
from blog.models import Blog, Comment
from django.db.models import Q
from product.models import Brand, Category, Product
from django.views.generic import DetailView, ListView
from blog.forms import CommentForm



class BlogDetailView(DetailView):
    model = Blog
    template_name = 'single-blog.html'

    def get_comment(self):
        return Comment.objects.filter(
            blog_id=self.kwargs.get('pk'))

    def get_qs_brand(self):
        return Brand.objects.all()

    def get_qs_category(self):
        return Category.objects.all()

    def get_qs_blogs(self):
        return Blog.objects.order_by('-create_at').exclude(pk=self.kwargs.get('pk'))

    def get_single_blog(self):
        return Blog.objects.get(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['comments'] = self.get_comment
        context['brands'] = self.get_qs_brand
        context['categories'] = self.get_qs_category
        context['blogs'] = self.get_qs_category
        context['relatedblogs'] = self.get_qs_blogs
        context['urlblog'] = self.get_single_blog
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment(
                description=request.POST.get('description'),
                blog_id=Blog.objects.get(pk=self.kwargs.get('pk')),
                user_id=request.user
            )
            comment.save()

            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = CommentForm
            return self.render_to_response(context=context)
        else:
            form = CommentForm()
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)


class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'

    def get_blogs(self):
        qs = Blog.objects.all()[0:3]
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = self.get_blogs()
        return context




def single_blog(request, pk):
    qs_one_blog = Blog.objects.get(pk=pk)
    qs_blogs = Blog.objects.order_by('-created_at').exclude(id=pk)
    qs_category = Category.objects.all()
    qs_comment = Comment.objects.filter(blog_id=pk)
    qs_brand = Brand.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                description=request.POST.get('description'),
                blog_id=Blog.objects.get(pk=pk),
                user_id=request.user
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
