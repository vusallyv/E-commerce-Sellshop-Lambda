from django.shortcuts import render, resolve_url

# Create your views here.

from django.db.models import Q, F
from product.models import Blog, Category, ProductVersion, Image, Review, Product, Comment, Brand, Size
from product.forms import CommentForm
from django.views.generic import DetailView, ListView, CreateView, View


# def product_list(request):
#     qs_productversion_all = ProductVersion.objects.all()
#     qs_productversion_best = ProductVersion.objects.order_by('-rating')[0]
#     qs_product = Product.objects.all()
#     qs_brand = Brand.objects.all()
#     qs = None
#     qs_size = Size.objects.all()

#     if request.GET.get("search_name"):
#         qs = ProductVersion.objects.filter(Q(product__title__icontains=request.GET.get("search_name")) | Q(
#             product__subtitle__icontains=request.GET.get("search_name")) | Q(product__description__icontains=request.GET.get("search_name")))
#     elif request.GET.get("category_name"):
#         qs_productversion_all = ProductVersion.objects.filter(
#             product__category__title=request.GET.get("category_name"))
#     elif request.GET.get("subcategory_name"):
#         qs_productversion_all = ProductVersion.objects.filter(
#             product__category__subcategories__title=request.GET.get("subcategory_name"))
#     elif request.GET.get("size"):
#         qs_productversion_all = ProductVersion.objects.filter(
#             size__title=request.GET.get("size"))
#     elif request.GET.get("brand"):
#         qs_productversion_all = ProductVersion.objects.filter(
#             product__brand__title=request.GET.get("brand"))
#     context = {
#         'title': 'Product-list Sellshop',
#         'productversions': qs,
#         'brands': qs_brand,
#         'allproductversions': qs_productversion_all[0:8],
#         'sizes': qs_size,
#         'bestproductversion': qs_productversion_best,
#         'products': qs_product,
#     }
#     return render(request, 'product-list.html', context=context)


class ProductListView(ListView):
    def get(self, request, *args, **kwargs):
        qs_productversion_all = ProductVersion.objects.all()
        if request.GET.get("search_name"):
            qs_productversion_all = ProductVersion.objects.filter(Q(product__title__icontains=request.GET.get("search_name")) | Q(
                product__subtitle__icontains=request.GET.get("search_name")) | Q(product__description__icontains=request.GET.get("search_name")))
        elif request.GET.get("category_name"):
            qs_productversion_all = ProductVersion.objects.filter(
                product__category__title=request.GET.get("category_name"))
        elif request.GET.get("subcategory_name"):
            qs_productversion_all = ProductVersion.objects.filter(
                product__category__subcategories__title=request.GET.get("subcategory_name"))
        elif request.GET.get("size"):
            qs_productversion_all = ProductVersion.objects.filter(
                size__title=request.GET.get("size"))
        elif request.GET.get("brand"):
            qs_productversion_all = ProductVersion.objects.filter(
                product__brand__title=request.GET.get("brand"))
        context = {
            'title': 'Product-list Sellshop',
            'products': qs_productversion_all,
            'sizes': Size.objects.all(),
            'categories': Category.objects.all(),
            'brands': Brand.objects.all()
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


class BlogDetailView(DetailView):
    def get_blog(self):
        return Blog.objects.get(pk=self.kwargs.get('pk'))

    def get_comment(self):
        return Comment.objects.get(blog_id=self.kwargs.get('pk'))

    def get_category(self):
        return Category.objects.all()

    def get_brand(self):
        return Brand.objects.all()

    def get_related_blog(self):
        return Blog.objects.order_by('-created_at').exclude(pk=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        context = {
            'comments': self.get_comment(),
            'title': 'Single-product Sellshop',
            'blog': self.get_blog(),
            'relatedblogs': self.get_related_blog(),
            'categories': self.get_category(),
            'brands': self.get_brand(),

        }
        return render(request, 'single-blog.html', context=context)


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'single-blog.html'

    def get_success_url(self):
        return resolve_url('product_list')


class ProductDetailView(DetailView):
    def get_product_version(self):
        return ProductVersion.objects.get(pk=self.kwargs.get('pk'))

    def get_reviews(self):
        try:
            return Review.objects.get(pk=self.kwargs.get('pk'))
        except Review.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        context = {
            'allproductversions': self.get_product_version(),
            'title': 'Single-product Sellshop',
            'reviews': self.get_reviews(),
        }
        return render(request, 'single-product.html', context=context)


def single_product(request, pk):
    qs_productversion_all = ProductVersion.objects.get(pk=pk)
    qs_reviews = Review.objects.all()
    context = {
        'title': 'Single-product Sellshop',
        'title': '',
        'allproductversions': qs_productversion_all,
        'reviews': qs_reviews,
    }
    return render(request, 'single-product.html', context=context)
