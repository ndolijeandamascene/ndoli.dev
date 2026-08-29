from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('language', 'Language'),
            ('backend', 'Backend / Framework'),
            ('database', 'Database & Vector'),
            ('ai', 'AI / Machine Learning'),
            ('infrastructure', 'Infrastructure & DevOps'),
            ('security', 'Security & Networking'),
            ('other', 'Other Tools'),
        ],
        default='backend'
    )
    icon_name = models.CharField(max_length=50, blank=True, help_text='Icon identifier or CSS class')

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('concept', 'Concept'),
        ('prototype', 'Prototype'),
        ('active_dev', 'Active Development'),
        ('production', 'Production'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    tagline = models.CharField(max_length=250, help_text='Concise one-liner summary')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='projects')
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='active_dev')
    role = models.CharField(max_length=100, default='Lead Developer / System Architect')
    featured = models.BooleanField(default=False, help_text='Highlight on homepage')
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)

    # High-level overview
    short_description = models.TextField(help_text='Card summary for list views')
    overview = models.TextField(blank=True, help_text='Detailed executive overview')

    # Case Study Deep-dive Sections
    problem_statement = models.TextField(blank=True, help_text='The real-world problem being solved')
    solution_architecture = models.TextField(blank=True, help_text='System design and architecture breakdown')
    implementation_details = models.TextField(blank=True, help_text='Key technical mechanisms, stack decisions')
    challenges_and_solutions = models.TextField(blank=True, help_text='Engineering hurdles overcome')
    security_and_governance = models.TextField(blank=True, help_text='Security, access controls, data safety')
    results_and_impact = models.TextField(blank=True, help_text='Outcomes, metrics (factual only)')
    lessons_learned = models.TextField(blank=True, help_text='Engineering takeaways')
    future_roadmap = models.TextField(blank=True, help_text='Planned features and iterations')

    # Links & Media
    repository_url = models.URLField(blank=True, help_text='GitHub repository URL')
    live_url = models.URLField(blank=True, help_text='Live demonstration or deployment')
    documentation_url = models.URLField(blank=True)
    hero_image = models.ImageField(upload_to='projects/', blank=True, null=True)

    # Metadata
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-featured', 'order', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'slug': self.slug})

    @property
    def status_label(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)
