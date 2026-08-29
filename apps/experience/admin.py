from django.contrib import admin
from .models import Experience, Education, SkillCategory, Skill, Certification

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 2


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level_tag', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    list_editable = ['is_featured', 'order']
    search_fields = ['name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'organization', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'organization']
    list_editable = ['order']
    search_fields = ['role', 'organization', 'description', 'responsibilities']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'graduation_year', 'is_visible', 'order']
    list_editable = ['is_visible', 'order']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuing_organization', 'issue_date', 'is_verified', 'order']
    list_filter = ['is_verified', 'issuing_organization']
