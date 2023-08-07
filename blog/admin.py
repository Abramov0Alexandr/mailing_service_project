from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'view_count', 'published_date')
    list_display_links = ('title',)
