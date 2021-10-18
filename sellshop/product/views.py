from django.shortcuts import render, resolve_url
from django.db.models import Q, F
from product.models import Category, ProductVersion, Image, Review, Product, Brand, Size,  Tag
from product.forms import ReviewForm
from django.views.generic import DetailView, ListView



class ProductDetailView(DetailView):
    model = ProductVersion
    template_name = 'single-product.html'

    # def get_image(self, pk):
    #     image = Image.objects.filter(productversion_id=pk)
    #     return image
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Single-product Sellshop'
        context['form'] = ReviewForm
        context['reviews'] = Review.objects.filter(
            product=self.kwargs.get('pk'))
        context['image'] = Image.objects.filter(
            productversion_id=self.kwargs.get('pk'))
        # context['image'] = self.get_image
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = Review(
                review=request.POST.get('review'),
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


class ProductListView(ListView):
    def get(self, request, *args, **kwargs):
        qs = None
        qs_productversion_all = ProductVersion.objects.all()

        if request.GET.get("search_name"):
            qs = ProductVersion.objects.filter(Q(product__title__icontains=request.GET.get("search_name")) | Q(
                product__subtitle__icontains=request.GET.get("search_name")) | Q(product__description__icontains=request.GET.get("search_name")))
        elif request.GET.get("category_name"):
            qs_productversion_all = ProductVersion.objects.filter(
                product__category_id__subcategory__title=request.GET.get("category_name"))
        elif request.GET.get("subcategory_name"):
            qs_productversion_all = ProductVersion.objects.filter(
                product__category_id__title=request.GET.get("subcategory_name"))
        elif request.GET.get("size"):
            qs_productversion_all = ProductVersion.objects.filter(
                size__title=request.GET.get("size"))
        elif request.GET.get("brand"):
            qs_productversion_all = ProductVersion.objects.filter(
                product__brand_id__title=request.GET.get("brand"))

        context = {
            'title': 'Product-list Sellshop',
            'productversions': qs,
            'allproductversions': qs_productversion_all[0:4],
            'images': Image.objects.all(),
            'sizes': Size.objects.all(),
            'categories': Category.objects.all(),
            'brands': Brand.objects.all(),
            'products': Product.objects.order_by('price')[0:6],
            

        }
        return render(request, 'product-list.html', context=context)


def single_product(request, pk):
    image = Image.objects.filter(productversion_id=pk)
    product = Product.objects.get(pk=pk)
    product_versions = ProductVersion.objects.get(pk=pk)
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
        'product': product,
        'form': form,
        'product_versions': product_versions,
        'reviews': review,
    }

    return render(request, 'single-product.html', context=context)


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
#             product__category_id__title=request.GET.get("category_name"))
#     elif request.GET.get("subcategory_name"):
#         qs_productversion_all = ProductVersion.objects.filter(
#             product__category__subcategories__title=request.GET.get("subcategory_name"))
#     elif request.GET.get("size"):
#         qs_productversion_all = ProductVersion.objects.filter(
#             size__title=request.GET.get("size"))
#     elif request.GET.get("brand"):
#         qs_productversion_all = ProductVersion.objects.filter(
#             product__brand_id__title=request.GET.get("brand"))
#     context = {
#         'title': 'Product-list Sellshop',
#         'productversions': qs,
#         'brands': qs_brand,
#         'allproductversions': qs_productversion_all[0:4],
#         'sizes': qs_size,
#         'bestproductversion': qs_productversion_best,
#         'products': qs_product,
#     }
#     return render(request, 'product-list.html', context=context)
