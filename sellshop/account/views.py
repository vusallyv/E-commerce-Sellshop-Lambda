from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def contact(request):
    context = {
        'title':  'Contact Us Sellshop'
    }
    return render(request, "contact.html", context=context)

def login(request):
    context = {
        'title':  'Login Sellshop'
    }
    return render(request, "login.html", context=context)

def my_account(request):
    context = {
        'title':  'My-account Sellshop'
    }
    return render(request, "my-account.html", context=context)