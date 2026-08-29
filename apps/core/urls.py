from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('hire/', views.HireMeView.as_view(), name='hire'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('cv/', views.CVView.as_view(), name='cv'),
    path('cv/pdf/', views.download_cv_pdf, name='cv_pdf'),
    path('now/', views.NowView.as_view(), name='now'),
]
