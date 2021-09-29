from django.contrib import admin

from blog.models import Comment, Blog

admin.site.register(Comment)
admin.site.register(Blog)