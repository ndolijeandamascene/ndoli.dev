from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Project, Category

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        queryset = Project.objects.filter(is_published=True).prefetch_related('technologies', 'category')
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['active_category'] = self.request.GET.get('category', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/detail.html'
    context_object_name = 'project'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Project.objects.filter(is_published=True).prefetch_related('technologies', 'category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.filter(
            is_published=True
        ).exclude(id=self.object.id).order_by('-featured', '?')[:3]
        return context
