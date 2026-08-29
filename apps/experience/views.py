from django.views.generic import TemplateView
from .models import Experience, Education, SkillCategory, Certification

class ExperienceView(TemplateView):
    template_name = 'experience/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.filter(is_visible=True)
        context['certifications'] = Certification.objects.filter(is_verified=True)
        return context


class SkillsView(TemplateView):
    template_name = 'skills/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all()
        return context
