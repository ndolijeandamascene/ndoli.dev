from django.db import models

class SiteSettings(models.Model):
    owner_name = models.CharField(max_length=150, default='NDOLI Jean Damascene')
    short_brand = models.CharField(max_length=50, default='NDOLI')
    role_title = models.CharField(max_length=200, default='IT Operations Administrator · Systems Administrator · Software Developer')
    hero_headline = models.CharField(
        max_length=300,
        default='I build practical digital systems, intelligent software, and technology solutions that solve real-world problems.'
    )
    snapshot_text = models.TextField(
        default='I am an IT professional and software developer focused on building practical digital systems. My work spans web applications, backend systems, databases, AI-assisted software, networking, cybersecurity, and technology solutions for real-world organizations.'
    )
    email = models.EmailField(default='ndolijeandamascene@gmail.com')
    location = models.CharField(max_length=100, default='Kigali, Rwanda')
    github_url = models.URLField(default='https://github.com/ndolijeandamascene', blank=True)
    linkedin_url = models.URLField(default='https://linkedin.com/in/ndoli-jean-damascene', blank=True)
    twitter_url = models.URLField(blank=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return f"Site Settings ({self.owner_name})"

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject} ({self.created_at.strftime('%Y-%m-%d %H:%M')})"


class JobOffer(models.Model):
    JOB_CATEGORY_CHOICES = [
        ('it_operations', 'IT Operations & Infrastructure'),
        ('systems_admin', 'Systems & Server Administration'),
        ('software_dev', 'Software & Web Development (Django/Python)'),
        ('helpdesk_support', 'ICT Help Desk & Technical Support'),
        ('ai_rag', 'AI, Vector Search & RAG Systems'),
        ('database_admin', 'Database Administration (PostgreSQL/MySQL)'),
        ('network_security', 'Networking & Cybersecurity'),
        ('it_management', 'IT Management & Leadership'),
        ('other', 'Other IT / Technology Role'),
    ]

    EMPLOYMENT_TYPE_CHOICES = [
        ('fulltime_onsite', 'Full-time (On-site)'),
        ('fulltime_hybrid', 'Full-time (Hybrid)'),
        ('fulltime_remote', 'Full-time (Remote)'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract / Project-based'),
        ('consulting', 'IT Consulting / Advisory'),
    ]

    STATUS_CHOICES = [
        ('new', 'New Offer'),
        ('reviewed', 'Reviewed'),
        ('contacted', 'Contacted / In Discussion'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('archived', 'Archived'),
    ]

    # Company & Contact Info
    company_name = models.CharField(max_length=150, help_text='Organization or Company offering the role')
    contact_person = models.CharField(max_length=120, help_text='Hiring Manager or Recruiter Name')
    contact_email = models.EmailField(help_text='Official or Business Email')
    contact_phone = models.CharField(max_length=50, blank=True, help_text='Phone / WhatsApp number')
    company_website = models.URLField(blank=True, help_text='Company website URL')

    # Job & Role Details
    job_title = models.CharField(max_length=150, help_text='e.g., IT Officer, Systems Administrator, Django Developer')
    job_category = models.CharField(max_length=50, choices=JOB_CATEGORY_CHOICES, default='it_operations')
    employment_type = models.CharField(max_length=40, choices=EMPLOYMENT_TYPE_CHOICES, default='fulltime_onsite')
    work_location = models.CharField(max_length=150, default='Kigali, Rwanda', help_text='Office city or Remote policy')
    
    # Compensation / Salary
    offered_salary = models.CharField(
        max_length=120,
        help_text='Proposed salary or budget (e.g., 1,500,000 RWF / month, $2,000 USD / month, or Negotiable)'
    )
    salary_currency = models.CharField(
        max_length=10,
        choices=[('RWF', 'RWF (Rwandan Franc)'), ('USD', 'USD ($)'), ('EUR', 'EUR (€)'), ('GBP', 'GBP (£)'), ('OTHER', 'Other')],
        default='RWF'
    )
    expected_start_date = models.CharField(max_length=100, default='Immediate / Next 30 Days', blank=True)

    # Job Description & Requirements
    job_description = models.TextField(help_text='Summary of role responsibilities, project scope, or required qualifications')
    
    # Metadata & Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Job Offer / Hiring Request'
        verbose_name_plural = 'Job Offers / Hiring Requests'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.offered_salary}) - {self.created_at.strftime('%Y-%m-%d')}"
