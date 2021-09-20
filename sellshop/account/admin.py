from django.contrib import admin

# Register your models here.

from account.models import Person, Contact

admin.site.register(Person)
admin.site.register(Contact)