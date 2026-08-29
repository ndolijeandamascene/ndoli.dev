from django.urls import path
from . import views

app_name = 'experience'

urlpatterns = [
    path('', views.ExperienceView.as_view(), name='list'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
]
