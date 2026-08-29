from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_name() if hasattr(views.ProjectListView, 'as_name') else views.ProjectListView.as_view(), name='list'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='detail'),
]
