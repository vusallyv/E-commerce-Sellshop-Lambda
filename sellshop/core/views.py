from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Sellshop'
        return context


def blog(request):
    context = {
        'title': 'Blog Sellshop',
    }
    return render(request, 'blog.html', context=context)


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
