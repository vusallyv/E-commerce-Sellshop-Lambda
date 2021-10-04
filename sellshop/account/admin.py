from django.contrib import admin

# Register your models here.

from account.models import Contact, User

admin.site.site_header = 'Sellshop Admin'
admin.site.site_title = 'Sellshop Admin'

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'city', 'salary')
#     list_filter = ('country','salary',)
#     list_editable = ('city',)
#     search_fields = ('first_name', )
#     # fields = ['first_name', 'city', 'salary'] #gormek istediyim fieldleri gosterir
#     # readonly_fields = ('salary',)
#     fieldsets = (
#         ('general informations', {'fields': ('first_name', 'last_name') }),
#         ('location informations', {'fields': ('country', 'city') }),
#         ('online informations', {'fields': ('email', 'phone_number', 'password','salary')}),
#         ('different informations', {'fields': ('additional_info',) }),
#     )

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email' )


admin.site.register([Contact])
