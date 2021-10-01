from django.shortcuts import render

# Create your views here.

from django.db.models import Q, F
from product.models import Blog, Category, ProductVersion, Image, Review, Product, Comment, Brand, Size
from product.forms import CommentForm
from django.views.generic import DetailView, ListView


def product_list(request):
    qs_productversion_all = ProductVersion.objects.all()
    qs_productversion_best = ProductVersion.objects.order_by('-rating')[0]
    qs_product = Product.objects.all()
    qs_brand = Brand.objects.all()
    qs = None
    qs_size = Size.objects.all()

    if request.GET.get("search_name"):
        qs = ProductVersion.objects.filter(Q(product__title__icontains=request.GET.get("search_name")) | Q(
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
        'productversions': qs,
        'brands': qs_brand,
        'allproductversions': qs_productversion_all[0:8],
        'sizes': qs_size,
        'bestproductversion': qs_productversion_best,
        'products': qs_product,
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
                description=request.POST.get('description')
            )
            comment.save()
    else:
        form = CommentForm()

    context = {
        'title': 'Single-blog Sellshop',
        'blogs': qs_blogs[0:3],
        'relatedblogs': qs_blogs,
        'firstblog': qs_one_blog,
        'categories': qs_category,
        'brands': qs_brand,
        'comments': qs_comment,
        'form': CommentForm,
    }
    return render(request, 'single-blog.html', context=context)


# class ProductDetailView(DetailView):
#     model = ProductVersion
#     template_name = 'single-product.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Single-product Sellshop'
#         return context


def single_product(request, pk):
    qs_productversion_all = ProductVersion.objects.get(pk=pk)
    qs_reviews = Review.objects.all()
    context = {
        'title': '',
        'allproductversions': qs_productversion_all,
        'reviews': qs_reviews,
    }
    return render(request, 'single-product.html', context=context)


class ProductListView(ListView):
    model = ProductVersion
    template_name = 'product-list.html'
    queryset = ProductVersion.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Product-list Sellshop'
        context['products'] = Product.objects.all()
        context['sizes'] = Size.objects.all()
        context['brands'] = Brand.objects.all()
        return context
