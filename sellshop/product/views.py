from django.shortcuts import render


from product.models import Category, Subcategory, ProductVersion, Product, Image,  Review

from django.db.models import Q
from product.forms import ReviewForm


def single_product(request):
    qs_image = Image.objects.all()
    qs = ProductVersion.objects.all()[0:1]
    review = Product.objects.all()[0:1]
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
   
    context = {
        'title': 'Single-product Sellshop',
        'products': qs,
        'review': review,
        'images': qs_image,
        'form': ReviewForm(),
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
