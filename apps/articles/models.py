from django.db import models
from django.urls import reverse
import markdown

class ArticleCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(help_text='Brief summary for cards and meta description')
    content = models.TextField(help_text='Article body in Markdown format')
    author_name = models.CharField(max_length=100, default='NDOLI Jean Damascene')
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, related_name='articles')
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    related_projects = models.ManyToManyField('projects.Project', related_name='articles', blank=True)
    cover_image = models.ImageField(upload_to='articles/', blank=True, null=True)
    reading_time_minutes = models.PositiveIntegerField(default=5)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})

    @property
    def rendered_content(self):
        return markdown.markdown(
            self.content,
            extensions=['fenced_code', 'codehilite', 'tables', 'toc', 'nl2br']
        )
