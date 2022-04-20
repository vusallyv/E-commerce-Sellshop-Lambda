from django.contrib import admin

# Register your models here.

from user.models import Contact, User, Subscriber

admin.site.site_header = 'Sellshop Admin'
admin.site.site_title = 'Sellshop Admin'


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'first_name', 'last_name',
#                     'email', 'is_staff', 'is_active', 'is_superuser', 'country', 'city')
#     list_filter = ('is_staff', 'is_active', 'is_superuser', 'country', 'city')
#     list_editable = ('is_staff', 'is_active', 'is_superuser')
#     # search_fields = ('first_name', )
#     # fields = ['first_name', 'city',]
#     # readonly_fields = ()
#     fieldsets = (
#         ('General information', {'fields': ('first_name', 'last_name')}),
#         ('Location information', {'fields': ('country', 'city')}),
#         ('Online information', {
#          'fields': ('username', 'email', 'phone_number', 'password',)}),
#         ('Different information', {
#          'fields': ('additional_info', 'is_staff', 'is_active', 'is_superuser')}),
#     )


# class UserAdmin(admin.ModelAdmin):


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message',)

admin.site.register([User, Subscriber])

