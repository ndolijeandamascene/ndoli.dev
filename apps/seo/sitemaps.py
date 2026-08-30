import urllib.parse
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.projects.models import Project
from apps.articles.models import Article

class CanonicalDomainSitemap(Sitemap):
    protocol = 'https'

    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(page=page, site=site, protocol='https')
        for url_info in urls:
            loc = url_info.get('location', '')
            parsed = urllib.parse.urlparse(loc)
            url_info['location'] = f"https://ndoli.dev{parsed.path}"
        return urls


class StaticViewSitemap(CanonicalDomainSitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return [
            ('core:home', 1.0, 'weekly'),
            ('core:about', 0.9, 'monthly'),
            ('projects:list', 0.9, 'weekly'),
            ('articles:list', 0.9, 'weekly'),
            ('experience:list', 0.8, 'monthly'),
            ('experience:skills', 0.8, 'monthly'),
            ('core:cv', 0.8, 'monthly'),
            ('core:contact', 0.7, 'monthly'),
            ('core:now', 0.6, 'monthly'),
        ]

    def location(self, item):
        return reverse(item[0])

    def priority(self, item):
        return item[1]

    def changefreq(self, item):
        return item[2]


class ProjectSitemap(CanonicalDomainSitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Project.objects.filter(is_published=True).order_by('order', '-created_at')

    def lastmod(self, obj):
        return obj.updated_at


class ArticleSitemap(CanonicalDomainSitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Article.objects.filter(is_published=True).order_by('-published_at')

    def lastmod(self, obj):
        return obj.updated_at
