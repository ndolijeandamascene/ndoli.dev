from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from apps.seo.sitemaps import StaticViewSitemap, ProjectSitemap, ArticleSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Core Pages (Home, About, Contact, CV, Now, etc.)
    path('', include('apps.core.urls')),

    # Projects & Case Studies
    path('projects/', include('apps.projects.urls')),

    # Technical Writing & Articles
    path('writing/', include('apps.articles.urls')),

    # Experience, Education & Skills
    path('experience/', include('apps.experience.urls')),

    # SEO, Sitemap & Robots.txt
    path('', include('apps.seo.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
