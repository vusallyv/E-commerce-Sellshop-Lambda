from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def my_account(request):
    return render(request, "my-account.html")