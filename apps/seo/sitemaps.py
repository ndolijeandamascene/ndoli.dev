from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.projects.models import Project
from apps.articles.models import Article

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return [
            'core:home',
            'core:about',
            'projects:list',
            'articles:list',
            'experience:list',
            'experience:skills',
            'core:cv',
            'core:now',
            'core:contact',
        ]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Project.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class ArticleSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Article.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at
