from django.http import HttpResponse
from django.views import View

class RobotsTxtView(View):
    def get(self, request):
        lines = [
            "User-agent: *",
            "Allow: /",
            "Allow: /about/",
            "Allow: /projects/",
            "Allow: /writing/",
            "Allow: /experience/",
            "Allow: /cv/",
            "Allow: /contact/",
            "Allow: /now/",
            "Allow: /static/",
            "Disallow: /admin/",
            "Disallow: /dashboard/",
            "Disallow: /login/",
            "Disallow: /logout/",
            "",
            "Sitemap: https://ndoli.dev/sitemap.xml",
        ]
        return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")
