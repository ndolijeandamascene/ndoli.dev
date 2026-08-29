from django.contrib import admin
from .models import ArticleCategory, Tag, Article

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'reading_time_minutes', 'is_featured', 'is_published', 'published_at']
    list_filter = ['is_published', 'is_featured', 'category', 'tags']
    list_editable = ['is_featured', 'is_published']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'excerpt', 'content']
    filter_horizontal = ['tags', 'related_projects']
