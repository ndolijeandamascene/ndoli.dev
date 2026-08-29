from django.db import models

class Experience(models.Model):
    organization = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    location = models.CharField(max_length=100, default='Rwanda')
    employment_type = models.CharField(max_length=50, default='Full-time')
    start_date = models.CharField(max_length=50, help_text='e.g., June 2023')
    end_date = models.CharField(max_length=50, blank=True, help_text='e.g., Present or May 2024')
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text='Brief overview of role scope')
    responsibilities = models.TextField(help_text='Bullet points (one per line)')
    technologies_used = models.CharField(max_length=250, blank=True, help_text='Comma-separated tech used')
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.role} at {self.organization}"

    @property
    def responsibilities_list(self):
        return [r.strip() for r in self.responsibilities.split('\n') if r.strip()]


class Education(models.Model):
    institution = models.CharField(max_length=150, default='University of Rwanda')
    degree = models.CharField(max_length=150, default='Bachelor of Science in Information Technology')
    field_of_study = models.CharField(max_length=100, default='Information Technology')
    graduation_year = models.CharField(max_length=20, default='2026')
    description = models.TextField(blank=True)
    is_visible = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} - {self.institution} ({self.graduation_year})"


class SkillCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Skill Category'
        verbose_name_plural = 'Skill Categories'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=80)
    level_tag = models.CharField(max_length=40, blank=True, help_text='e.g., Core, Advanced, Tool')
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Certification(models.Model):
    name = models.CharField(max_length=150)
    issuing_organization = models.CharField(max_length=150)
    issue_date = models.CharField(max_length=50, blank=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    is_verified = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Certification'
        verbose_name_plural = 'Certifications'
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.name} - {self.issuing_organization}"
