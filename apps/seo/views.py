from django.http import HttpResponse
from django.views import View

class RobotsTxtView(View):
    def get(self, request):
        lines = [
            "User-agent: *",
            "Allow: /",
            "Disallow: /admin/",
            "",
            "Sitemap: https://ndoli.dev/sitemap.xml",
        ]
        return HttpResponse("\n".join(lines), content_type="text/plain")
