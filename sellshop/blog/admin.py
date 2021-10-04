from django.contrib import admin
from blog.models import Comment, Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator',)
    list_filter = ('creator',)


admin.site.register([Comment])
