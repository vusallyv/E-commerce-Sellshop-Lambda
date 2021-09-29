from django.contrib import admin

# Register your models here.

from account.models import Contact, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email' )


admin.site.register([Contact])
