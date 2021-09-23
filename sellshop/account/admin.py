from django.contrib import admin

# Register your models here.

from account.models import Contact, User

admin.site.register([Contact, User])
