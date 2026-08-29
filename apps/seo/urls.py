from django.urls import path
from .views import RobotsTxtView

app_name = 'seo'

urlpatterns = [
    path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
]
