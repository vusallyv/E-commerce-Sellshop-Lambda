from django.db.models.aggregates import Avg
from django.shortcuts import render
from django.db.models import Q, F
from product.models import Category, ProductVersion, Image, Review, Product, Brand, Size,  Tag
from product.forms import ReviewForm
from django.views.generic import DetailView, ListView


def single_product(request, pk):
    image = Image.objects.filter(productversion=pk)
    product_versions = ProductVersion.objects.get(pk=pk)
    related_products = ProductVersion.objects.exclude(pk=pk)
    review = Review.objects.filter(product=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = Review(
                user=request.user,
                review=request.POST.get('review'),
                product=ProductVersion.objects.get(pk=pk),
            )
            form.save()
    else:
        form = ReviewForm()

    context = {
        'title': 'Single-product Sellshop',
        'images': image,
        'form': form,
        'productversion': product_versions,
        'relatedproducts': related_products,
        'reviews': review,
    }

    return render(request, 'single-product.html', context=context)


class ProductDetailView(DetailView):
    model = ProductVersion
    template_name = 'single-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Single-product Sellshop'
        context['images'] = Image.objects.filter(
            productversion=self.kwargs.get('pk'))
        context['form'] = ReviewForm
        context['rating'] = "{:.1f}".format(Review.objects.filter(
            product=self.kwargs.get('pk')).aggregate(Avg('rating'))['rating__avg'])
        context['reviews'] = Review.objects.filter(
            product=self.kwargs.get('pk'))
        context['productversion'] = ProductVersion.objects.get(
            pk=self.kwargs.get('pk'))
        context['relatedproducts'] = ProductVersion.objects.exclude(
            pk=self.kwargs.get('pk'))
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = Review(
                review=request.POST.get('review'),
                rating=request.POST.get('rating'),
                product=ProductVersion.objects.get(pk=self.kwargs.get('pk')),
                user=request.user
            )
            review.save()

            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)
        else:
            form = ReviewForm()
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)


def product_list(request):
    qs_productversion_all = ProductVersion.objects.all()
    qs_productversion_best = ProductVersion.objects.order_by('-rating')[0]
    qs_product = Product.objects.all()
    qs_brand = Brand.objects.all()
    qs_category = Category.objects.all()
    qs = None
    qs_size = Size.objects.all()

    if request.GET.get("search_name"):
        qs = ProductVersion.objects.filter(Q(product__title__icontains=request.GET.get("search_name")) | Q(
            product__subtitle__icontains=request.GET.get("search_name")) | Q(product__description__icontains=request.GET.get("search_name")))
    elif request.GET.get("category_name"):
        qs_productversion_all = ProductVersion.objects.filter(
            product__category__parent__title=request.GET.get("category_name"))
    elif request.GET.get("subcategory_name"):
        qs_productversion_all = ProductVersion.objects.filter(
            product__category__title=request.GET.get("subcategory_name"))
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
        'categories': qs_category,
        'allproductversions': qs_productversion_all[0:4],
        'sizes': qs_size,
        'bestproductversion': qs_productversion_best,
        'products': qs_product,
    }
    return render(request, 'product-list.html', context=context)


class ProductListView(ListView):
    model = Product
    template_name = 'product-list.html'

    def get(self, request, *args, **kwargs):
        qs = None
        qs_productversion_all = ProductVersion.objects.all()

        if request.GET.get("search_name"):
            qs = ProductVersion.objects.filter(Q(product__title__icontains=request.GET.get("search_name")) | Q(
                product__subtitle__icontains=request.GET.get("search_name")) | Q(product__description__icontains=request.GET.get("search_name")))
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
            'allproductversions': qs_productversion_all[0:4],
            'sizes': Size.objects.all(),
            'categories': Category.objects.all(),
            'brands': Brand.objects.all(),
            'products': Product.objects.order_by('price')[0:6],
        }
        return render(request, 'product-list.html', context=context)


# def filter(request):
#     if request.GET.get('size'):
#         current_path = request.get_full_path()
#         print(current_path)
#     context = {
#         'current_path': current_path
#     }
#     return render(request, "product-list.html", context=context)
