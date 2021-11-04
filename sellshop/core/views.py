from django.shortcuts import redirect, render
from blog.models import Blog
from django.db.models import Q
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from user.forms import ContactForm, SubscriberForm
# Create your views here.


def about(request):
    if request.method == 'POST' and "contact" in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    if request.method == 'POST' and 'subscribe' in request.POST:
        subscribe = SubscriberForm(request.POST)
        if subscribe.is_valid():
            subscribe.save()
            return redirect('contact')
    else:
        subscribe = SubscriberForm()

    context = {
        'title':  'About Sellshop',
        'contactform': form,
        'subscribeform': subscribe,
    }
    return render(request, "about.html", context=context)


class BaseView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Sellshop'
        return context


def index(request):
    context = {
        'title': 'Home Sellshop',
    }
    return render(request, 'index.html', context=context)


class ErrorView(TemplateView):
    template_name = 'error-404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Error Sellshop'
        return context


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Sellshop'
        return context


def change_language(request):
    if request.GET.get('lang') == 'en' or request.GET.get('lang') == 'az' or request.GET.get('lang') == 'ru':
        # print(request.META.get('HTTP_REFERER'))
        path_list = request.META.get('HTTP_REFERER').split('/')
        # print(path_list)
        path_list[3] = request.GET.get('lang')
        path = '/'.join(path_list)
        # print(path)

        response = HttpResponseRedirect(path)
        response.set_cookie('django_language', request.GET['lang'])
        return response
