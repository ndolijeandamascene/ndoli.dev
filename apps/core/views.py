from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from .forms import ContactForm, JobOfferForm
from .models import SiteSettings, JobOffer
from apps.projects.models import Project
from apps.articles.models import Article
from apps.experience.models import Experience, Education, SkillCategory

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flagship_project'] = Project.objects.filter(slug='ihkip', is_published=True).first()
        context['selected_projects'] = Project.objects.filter(
            is_published=True
        ).prefetch_related('technologies')[:6]
        context['recent_articles'] = Article.objects.filter(
            is_published=True
        ).select_related('category')[:3]
        context['experiences'] = Experience.objects.all()[:5]
        context['education'] = Education.objects.filter(is_visible=True).first()
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all()
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educations'] = Education.objects.filter(is_visible=True)
        context['experiences'] = Experience.objects.all()
        return context


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        contact_msg = form.save(commit=False)
        # Capture client IP
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            contact_msg.ip_address = x_forwarded_for.split(',')[0]
        else:
            contact_msg.ip_address = self.request.META.get('REMOTE_ADDR')
        contact_msg.save()
        messages.success(self.request, "Thank you for reaching out! Your message has been sent successfully. I will get back to you soon.")
        return super().form_valid(form)


class HireMeView(FormView):
    template_name = 'core/hire.html'
    form_class = JobOfferForm
    success_url = reverse_lazy('core:hire')

    def form_valid(self, form):
        job_offer = form.save(commit=False)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            job_offer.ip_address = x_forwarded_for.split(',')[0]
        else:
            job_offer.ip_address = self.request.META.get('REMOTE_ADDR')
        job_offer.save()
        messages.success(
            self.request,
            f"Thank you, {job_offer.contact_person}! Your job offer for '{job_offer.job_title}' at {job_offer.company_name} has been received. I will review the compensation and role requirements and reply promptly."
        )
        return super().form_valid(form)


class CVView(TemplateView):
    template_name = 'core/cv.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiences'] = Experience.objects.all()
        context['educations'] = Education.objects.filter(is_visible=True)
        context['skill_categories'] = SkillCategory.objects.prefetch_related('skills').all()
        context['featured_projects'] = Project.objects.filter(is_published=True, featured=True)
        return context


def download_cv_pdf(request):
    import os
    from django.conf import settings
    from django.http import FileResponse, Http404
    pdf_path = os.path.join(settings.BASE_DIR, 'static', 'docs', 'NDOLI_Jean_Damascene_CV.pdf')
    if not os.path.exists(pdf_path):
        pdf_path = os.path.join(settings.BASE_DIR, 'NDOLI_Jean_Damascene_CV.pdf')
    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf', as_attachment=False, filename='NDOLI_Jean_Damascene_CV.pdf')
    raise Http404("CV PDF not found.")


class NowView(TemplateView):
    template_name = 'core/now.html'


def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)
