from django.shortcuts import render

from account.forms import ContactForm



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()
    context = {
        'title':  'Contact Us Sellshop',
        'form': ContactForm(),
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