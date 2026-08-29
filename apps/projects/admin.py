from django.contrib import admin
from .models import Category, Technology, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'icon_name']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'featured', 'is_published', 'order', 'created_at']
    list_filter = ['status', 'featured', 'is_published', 'category', 'technologies']
    list_editable = ['featured', 'is_published', 'order']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'tagline', 'short_description', 'overview']
    filter_horizontal = ['technologies']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'tagline', 'category', 'technologies', 'status', 'role', 'featured', 'order', 'is_published')
        }),
        ('Overview', {
            'fields': ('short_description', 'overview', 'hero_image')
        }),
        ('Deep-Dive Case Study', {
            'fields': (
                'problem_statement',
                'solution_architecture',
                'implementation_details',
                'challenges_and_solutions',
                'security_and_governance',
                'results_and_impact',
                'lessons_learned',
                'future_roadmap',
            ),
            'classes': ('collapse',),
        }),
        ('Links', {
            'fields': ('repository_url', 'live_url', 'documentation_url')
        }),
    )
