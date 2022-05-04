from django.contrib import admin
from blog.models import Comment, Blog
from blog.forms import CommentForm


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator',)
    list_filter = ('creator',)
    exclude = ('slug',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    exclude = ('is_main',)
    form = CommentForm
