from django.contrib import admin
from .models import SiteSettings, ContactMessage, JobOffer, Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'role_title', 'organization', 'project_context', 'is_featured', 'order']
    list_filter = ['is_featured', 'created_at']
    list_editable = ['is_featured', 'order']
    search_fields = ['client_name', 'role_title', 'organization', 'quote']

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['owner_name', 'role_title', 'email', 'location']

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read', 'ip_address']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at', 'ip_address']
    search_fields = ['name', 'email', 'subject', 'message']


@admin.register(JobOffer)
class JobOfferAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company_name', 'contact_person', 'offered_salary', 'salary_currency', 'employment_type', 'status', 'created_at']
    list_filter = ['status', 'job_category', 'employment_type', 'salary_currency', 'created_at']
    list_editable = ['status']
    search_fields = ['company_name', 'contact_person', 'contact_email', 'job_title', 'job_description']
    readonly_fields = ['created_at', 'ip_address']
    fieldsets = (
        ('Company & Recruiter Details', {
            'fields': ('company_name', 'contact_person', 'contact_email', 'contact_phone', 'company_website')
        }),
        ('Role & IT Specialization', {
            'fields': ('job_title', 'job_category', 'employment_type', 'work_location', 'expected_start_date')
        }),
        ('Proposed Compensation & Description', {
            'fields': ('offered_salary', 'salary_currency', 'job_description')
        }),
        ('Status & Metadata', {
            'fields': ('status', 'created_at', 'ip_address')
        }),
    )
