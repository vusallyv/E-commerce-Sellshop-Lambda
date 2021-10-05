from django.shortcuts import render, resolve_url
from django.db.models import Q, F
from product.models import Category, ProductVersion, Image, Review, Product, Brand, Size,  Tag
from product.forms import ReviewForm
from django.views.generic import DetailView, ListView


def single_product(request, pk):
    image = Image.objects.get(pk=pk)
    product = Product.objects.get(pk=pk)
    product_versions = ProductVersion.objects.get(pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReviewForm()
    else:
        form = ReviewForm()

    context = {
        'title': 'Single-product Sellshop',
        'images': image,
        'product': product,
        'form': ReviewForm(),
        'product_versions': product_versions
    }

    return render(request, 'single-product.html', context=context)


# def product_list(request):
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


# def product_list(request):
#     products = Product.objects.order_by('price')[0:4]
#     images = Image.objects.all()
#     categories = Category.objects.all()

#     context = {
#         'title': 'Product-list Sellshop',
#         'products': products,
#         'images': images,
#         'categories': categories,
#     }
#     return render(request, 'product-list.html', context=context)


# class Product_list(ListView):
    model = Image
    template_name = 'practic_list.html'
    # queryset = Image.objects.order_by('image')[0:1]

    def get_queryset(self):
        qs = Image.objects.order_by('image')[0:1]
        return qs


class Product_list(ListView):
    model = Image
    template_name = 'practic_list.html'

    def get_image(self):
        return Image.objects.all()
    
    def get_products(self):
        return Product.objects.order_by('price')[0:4]
    
    def get_categories(self):
        return Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.get_image
        context['products'] = self.get_products
        return context
        
    



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
