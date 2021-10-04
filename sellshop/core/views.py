from django.shortcuts import render
from blog.models import Blog
from django.db.models import Q
from django.views.generic import TemplateView

# Create your views here.


def about(request):
    context = {
        'title': 'About Sellshop',
    }
    return render(request, 'about.html', context=context)


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
