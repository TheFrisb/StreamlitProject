from django.contrib import admin
from .models import BlogCategory, BlogPost
# Register your models here.


class BlogCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('name',)


class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    exclude = ('truncated_content', 'truncated_title')
    list_display = ('id', 'title', 'category', 'created_at')
    search_fields = ('title', 'content') # this enables django admin search functionality for these fields
    list_filter = ('category',) # this enables django admin filter functionality by category


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)

