from datetime import datetime
from django.db.models.aggregates import Avg, Count
from django.shortcuts import redirect, render
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from product.models import Category, Color, ProductVersion, Image, Review, Product, Brand, Size,  Tag
from user.models import User
from product.forms import ReviewForm
from django.views.generic import DetailView, ListView


class ProductDetailView(DetailView):
    model = ProductVersion
    template_name = 'single-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Single-product Sellshop'
        context['images'] = Image.objects.filter(
            productversion=self.kwargs.get('pk'))
        context['form'] = ReviewForm
        context['productversion'] = ProductVersion.objects.get(
            pk=self.kwargs.get('pk'))
        context['relatedproducts'] = ProductVersion.objects.filter(Q(product__brand=ProductVersion.objects.get(pk=self.kwargs.get('pk')).product.brand) |
                                                                   Q(product__category=ProductVersion.objects.get(pk=self.kwargs.get('pk')).product.category)).exclude(pk=self.kwargs.get('pk'))[0:3]
        context['product_color'] = ProductVersion.objects.all()
        context['form'] = ReviewForm
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'

    def get(self, request, *args, **kwargs):
        qs = None
        qs_productversion_all = ProductVersion.objects.filter(
            is_main=True).order_by('created_at')

        if request.GET:
            qs_productversion_all = ProductVersion.objects.all()
            if request.GET.get("category_name"):
                qs_productversion_all = ProductVersion.objects.filter(
                    product__category__parent__title=request.GET.get("category_name"))
            if request.GET.get("subcategory_name"):
                qs_productversion_all = qs_productversion_all.filter(
                    product__category__title=request.GET.get("subcategory_name"))
            if request.GET.get("size"):
                qs_productversion_all = qs_productversion_all.filter(
                    size__title=request.GET.get("size"))
            if request.GET.get("brand"):
                qs_productversion_all = qs_productversion_all.filter(
                    product__brand__title=request.GET.get("brand"))
            if request.GET.get("color"):
                qs_productversion_all = qs_productversion_all.filter(
                    color__hex_code=request.GET.get("color"))
            if request.GET.get("min_price"):
                qs_productversion_all = qs_productversion_all.filter(
                    product__price__gte=request.GET.get("min_price"))
            if request.GET.get("max_price"):
                qs_productversion_all = qs_productversion_all.filter(
                    product__price__lte=request.GET.get("max_price"))
        context = {
            'title': 'Product-list Sellshop',
            'productversions': qs,
            'images': Image.objects.filter(is_main=True),
            'allproductversions': qs_productversion_all,
            'sizes': Size.objects.all(),
            'categories': Category.objects.all(),
            'brands': Brand.objects.all(),
            'colors': Color.objects.all(),
            'products': Product.objects.order_by('price')[0:6],
        }
        return render(request, 'product-list.html', context=context)



def PaginatorProductList(request):
    product_list = ProductVersion.objects.filter(
        is_main=True).order_by('created_at')
    product_len = ProductVersion.objects.filter(is_main=True).count()

    paginator = Paginator(product_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.GET:
        product_list = ProductVersion.objects.order_by('created_at')
        if request.GET.get("category_name"):
            product_list = product_list.filter(
                product__category__parent__title=request.GET.get("category_name"))
        if request.GET.get("subcategory_name"):
            product_list = product_list.filter(
                product__category__title=request.GET.get("subcategory_name"))
        if request.GET.get("size"):
            product_list = product_list.filter(
                size__title=request.GET.get("size"))
        if request.GET.get("brand"):
            product_list = product_list.filter(
                product__brand__title=request.GET.get("brand"))
        if request.GET.get("color"):
            product_list = product_list.filter(
                color__title=request.GET.get("color"))
        if request.GET.get("min_price"):
            product_list = product_list.filter(
                product__price__gte=request.GET.get("min_price"))
        if request.GET.get("max_price"):
            product_list = product_list.filter(
                product__price__lte=request.GET.get("max_price"))
        paginator = Paginator(product_list, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': 'Product-list Sellshop',
        'images': Image.objects.filter(is_main=True),
        'sizes': Size.objects.all(),
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
        'colors': Color.objects.all(),
        'product_len': product_len,
        'best': ProductVersion.objects.annotate(
        mostsold=Count('Product_Cart')).order_by('-mostsold')[0]
    }
    return render(request, 'product-list.html', context=context)


class SearchView(ListView):
    model = Product
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        qs = None
        if request.GET:
            if request.GET.get("search_name"):
                qs = ProductVersion.objects.filter(Q(product__title__icontains=request.GET.get("search_name")) | Q(
                    product__subtitle__icontains=request.GET.get("search_name")) | Q(product__description__icontains=request.GET.get("search_name"))).filter(is_main=True)

        context = {
            'title': 'Product-list Sellshop',
            'productversions': qs,
            'images': Image.objects.filter(is_main=True),
            'word': request.GET.get("search_name"),
            'quantity': len(qs)
        }
        return render(request, 'search.html', context=context)
