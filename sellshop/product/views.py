from django.shortcuts import render

from django.views.generic import View, ListView
from product.models import Category, Subcategory, Product, Image, ProductVersion, Tag
from django.db.models import Q
from product.forms import ReviewForm


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



def product_list(request):
    products = Product.objects.order_by('price')[0:4]
    images = Image.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    
    context = {
        'title': 'Product-list Sellshop',
        'products': products,
        'images': images,
        'categories': categories,
        'subcategories': subcategories,
    }
    return render(request, 'product-list.html', context=context)


# class Product_list(View):
    
    def get_object(self):
        return Product.objects.get(pk=self.kwargs['pk'])
        
    def get_source(self):
        sources = self.request.COOKIES.get('utm_source')
        sources = sources.split(',')
        return sources
    
    def get(self, request, *args, **kwargs):
        context = {
            'sources': self.get_source(),
            'product_list': self.get_object(),
        }
    
        return render(request,'product-list.html',context=context)
    
# class Product_list(ListView):
#     model = Image
#     template_name = 'practic_list.html'
#     # queryset = Image.objects.order_by('image')[0:1]
    
#     def get_queryset(self):
#         qs = Image.objects.order_by('image')[0:1]
#         return qs
    
class Product_list(ListView):
    
    model = Image
    template_name = 'practic_list.html'
    def get_queryset(self):
        qs = Image.objects.order_by('image')[0:4]
        return qs
    
    # model = Product
    # template_name = 'practic_list.html'
    # def get_queryset(self):
    #     qs = Product.objects.order_by('price')[0:4]
    #     return qs
    
    # model = Category
    # template_name = 'practic_list.html'
    # def get_queryset(self):
    #     qs = Category.objects.all()
    #     return qs
    
    # model = Subcategory
    # template_name = 'practic_list.html'
    # def get_queryset(self):
    #     qs = Subcategory.objects.all()
    #     return qs
    
        
        
    