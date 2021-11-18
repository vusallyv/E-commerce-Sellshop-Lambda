from django.shortcuts import redirect, render
from blog.models import Blog
from django.db.models import Count, Q
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect
from product.models import Color, Image, ProductVersion

from user.forms import ContactForm, SubscriberForm
# Create your views here.


def about(request):
    context = {
        'title':  'About Sellshop',
    }
    return render(request, "about.html", context=context)


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Sellshop'
        return context


def index(request):
    new_arrivals = ProductVersion.objects.order_by("-created_at")
    mostreview = ProductVersion.objects.annotate(
        num_rev=Count('product_reviews')).order_by('-num_rev')[:6]
    bestseller = ProductVersion.objects.annotate(
        mostsold=Count('Product_Cart')).order_by('-mostsold')[1:8]
    firstbestseller = ProductVersion.objects.annotate(
        mostsold=Count('Product_Cart')).order_by('-mostsold')[0]
    latest_blog = Blog.objects.order_by("-created_at")[:3]
    images = Image.objects.filter(is_main=True)
    productversions = ProductVersion.objects.all()
    context = {
        'title': 'Home Sellshop',
        'mostreview': mostreview,
        'new_arrivals': new_arrivals,
        'latest_blog': latest_blog,
        'images': images,
        'bestseller': bestseller,
        'firstbestseller': firstbestseller,
        'productversions': productversions,
    }
    return render(request, 'index.html', context=context)


class ErrorView(TemplateView):
    template_name = 'error-404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Error Sellshop'
        return context


def change_language(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'az' or request.GET.get('lang') == 'ru':
        path_list = request.META.get('HTTP_REFERER').split('/')
        path_list[3] = request.GET.get('lang')
        path = '/'.join(path_list)
        response = HttpResponseRedirect(path)
        response.set_cookie('django_language', request.GET['lang'])
        return response
