from django.shortcuts import render
from blog.models import Blog
from django.db.models import Q
# Create your views here.



def about(request):
    context = {
        'title': 'About Sellshop',
    }
    return render(request, 'about.html', context=context)




def error_404(request):
    context = {
        'title': 'Error Sellshop',
    }
    return render(request, 'error-404.html', context=context)


def index(request):
    context = {
        'title': 'Home Sellshop',
    }
    return render(request, 'index.html', context=context)


