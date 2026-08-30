from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, JobOfferForm
from .models import SiteSettings, ContactMessage, JobOffer, Testimonial
from apps.projects.models import Project, Category, Technology
from apps.articles.models import Article, ArticleCategory
from apps.experience.models import Experience, Education, SkillCategory, Skill, Certification

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
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)
        return context


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educations'] = Education.objects.filter(is_visible=True)
        context['experiences'] = Experience.objects.all()
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)
        return context


class ContactView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('core:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)
        return context

    def form_valid(self, form):
        contact_msg = form.save(commit=False)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            contact_msg.ip_address = x_forwarded_for.split(',')[0]
        else:
            contact_msg.ip_address = self.request.META.get('REMOTE_ADDR')
        contact_msg.save()

        # Send Email Notification
        try:
            recipient = getattr(settings, 'OWNER_EMAIL', 'ndolijeandamascene@gmail.com')
            send_mail(
                subject=f"[ndoli.dev] New Message from {contact_msg.name}: {contact_msg.subject}",
                message=f"Name: {contact_msg.name}\nEmail: {contact_msg.email}\nSubject: {contact_msg.subject}\nIP: {contact_msg.ip_address}\n\nMessage:\n{contact_msg.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=True,
            )
        except Exception:
            pass

        messages.success(self.request, "Thank you for reaching out! Your message has been sent successfully. I will get back to you soon.")
        return super().form_valid(form)


class HireMeView(FormView):
    template_name = 'core/hire.html'
    form_class = JobOfferForm
    success_url = reverse_lazy('core:hire')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)
        return context

    def form_valid(self, form):
        job_offer = form.save(commit=False)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            job_offer.ip_address = x_forwarded_for.split(',')[0]
        else:
            job_offer.ip_address = self.request.META.get('REMOTE_ADDR')
        job_offer.save()

        # Send Email Notification
        try:
            recipient = getattr(settings, 'OWNER_EMAIL', 'ndolijeandamascene@gmail.com')
            send_mail(
                subject=f"[ndoli.dev] New Job Proposal: {job_offer.job_title} at {job_offer.company_name}",
                message=(
                    f"A new job offer / hiring proposal has been submitted on ndoli.dev:\n\n"
                    f"Company: {job_offer.company_name}\n"
                    f"Contact Person: {job_offer.contact_person}\n"
                    f"Email: {job_offer.contact_email}\n"
                    f"Phone: {job_offer.contact_phone}\n"
                    f"Website: {job_offer.company_website}\n\n"
                    f"Role: {job_offer.job_title}\n"
                    f"Category: {job_offer.get_job_category_display()}\n"
                    f"Type: {job_offer.get_employment_type_display()}\n"
                    f"Location: {job_offer.work_location}\n"
                    f"Offered Salary: {job_offer.offered_salary} {job_offer.salary_currency}\n"
                    f"Expected Start Date: {job_offer.expected_start_date}\n\n"
                    f"Description / Scope:\n{job_offer.job_description}\n"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=True,
            )
        except Exception:
            pass

        messages.success(
            self.request,
            f"Thank you, {job_offer.contact_person}! Your job offer for '{job_offer.job_title}' at {job_offer.company_name} has been received. I will review the compensation and role requirements and reply promptly."
        )
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('core:dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)


def custom_logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out of the control dashboard.")
    return redirect('core:home')


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Summary counts
        context['projects_count'] = Project.objects.count()
        context['live_projects_count'] = Project.objects.filter(status='production').count()
        context['prototype_count'] = Project.objects.filter(status='prototype').count()
        context['all_projects'] = Project.objects.all().order_by('order', '-created_at')
        context['project_categories'] = Category.objects.all()
        
        context['articles_count'] = Article.objects.count()
        context['published_articles_count'] = Article.objects.filter(is_published=True).count()
        context['all_articles'] = Article.objects.all().order_by('-published_at', '-updated_at')
        context['article_categories'] = ArticleCategory.objects.all()
        
        context['messages_count'] = ContactMessage.objects.count()
        context['unread_messages_count'] = ContactMessage.objects.filter(is_read=False).count()
        context['all_messages'] = ContactMessage.objects.all().order_by('-created_at')
        context['recent_messages'] = context['all_messages'][:5]

        context['job_offers_count'] = JobOffer.objects.count()
        context['new_job_offers_count'] = JobOffer.objects.filter(status='new').count()
        context['all_job_offers'] = JobOffer.objects.all().order_by('-created_at')
        context['recent_job_offers'] = context['all_job_offers'][:5]

        context['experiences_count'] = Experience.objects.count()
        context['skills_count'] = Skill.objects.count()
        context['certifications_count'] = Certification.objects.count()

        context['site_settings'] = SiteSettings.load()
        return context

    def post(self, request, *args, **kwargs):
        from django.utils.text import slugify
        action = request.POST.get('action')

        # ================= PROJECTS CRUD =================
        # CREATE PROJECT
        if action == 'add_project':
            title = request.POST.get('title', '').strip()
            if title:
                slug = slugify(title)
                base_slug = slug
                counter = 1
                while Project.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                
                cat_id = request.POST.get('category')
                cat = Category.objects.filter(id=cat_id).first() if cat_id else None

                Project.objects.create(
                    title=title,
                    slug=slug,
                    tagline=request.POST.get('tagline', '').strip(),
                    category=cat,
                    status=request.POST.get('status', 'active_dev'),
                    role=request.POST.get('role', 'Lead Developer').strip(),
                    live_url=request.POST.get('live_url', '').strip(),
                    repository_url=request.POST.get('repository_url', '').strip(),
                    short_description=request.POST.get('short_description', '').strip(),
                    overview=request.POST.get('overview', '').strip(),
                    problem_statement=request.POST.get('problem_statement', '').strip(),
                    solution_architecture=request.POST.get('solution_architecture', '').strip(),
                    featured=bool(request.POST.get('featured')),
                    is_published=True,
                )
                messages.success(request, f"Project '{title}' created successfully!")

        # UPDATE PROJECT
        elif action == 'edit_project':
            proj_id = request.POST.get('project_id')
            proj = Project.objects.filter(id=proj_id).first()
            if proj:
                proj.title = request.POST.get('title', proj.title).strip()
                proj.tagline = request.POST.get('tagline', proj.tagline).strip()
                cat_id = request.POST.get('category')
                if cat_id:
                    proj.category = Category.objects.filter(id=cat_id).first()
                proj.status = request.POST.get('status', proj.status)
                proj.role = request.POST.get('role', proj.role).strip()
                proj.live_url = request.POST.get('live_url', proj.live_url).strip()
                proj.repository_url = request.POST.get('repository_url', proj.repository_url).strip()
                proj.short_description = request.POST.get('short_description', proj.short_description).strip()
                proj.overview = request.POST.get('overview', proj.overview).strip()
                proj.featured = bool(request.POST.get('featured'))
                proj.save()
                messages.success(request, f"Project '{proj.title}' updated successfully!")

        # DELETE PROJECT
        elif action == 'delete_project':
            proj_id = request.POST.get('project_id')
            proj = Project.objects.filter(id=proj_id).first()
            if proj:
                p_title = proj.title
                proj.delete()
                messages.success(request, f"Project '{p_title}' was deleted.")

        # ================= ARTICLES CRUD =================
        # CREATE ARTICLE
        elif action == 'add_article':
            title = request.POST.get('title', '').strip()
            if title:
                slug = slugify(title)
                base_slug = slug
                counter = 1
                while Article.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                cat_id = request.POST.get('category')
                cat = ArticleCategory.objects.filter(id=cat_id).first() if cat_id else None

                Article.objects.create(
                    title=title,
                    slug=slug,
                    category=cat,
                    excerpt=request.POST.get('excerpt', '').strip(),
                    content=request.POST.get('content', '').strip(),
                    reading_time_minutes=int(request.POST.get('reading_time_minutes', 5) or 5),
                    is_published=bool(request.POST.get('is_published', True)),
                    is_featured=bool(request.POST.get('is_featured')),
                )
                messages.success(request, f"Article '{title}' has been published!")

        # UPDATE ARTICLE
        elif action == 'edit_article':
            art_id = request.POST.get('article_id')
            art = Article.objects.filter(id=art_id).first()
            if art:
                art.title = request.POST.get('title', art.title).strip()
                art.excerpt = request.POST.get('excerpt', art.excerpt).strip()
                art.content = request.POST.get('content', art.content).strip()
                cat_id = request.POST.get('category')
                if cat_id:
                    art.category = ArticleCategory.objects.filter(id=cat_id).first()
                art.reading_time_minutes = int(request.POST.get('reading_time_minutes', art.reading_time_minutes) or 5)
                art.is_published = bool(request.POST.get('is_published'))
                art.is_featured = bool(request.POST.get('is_featured'))
                art.save()
                messages.success(request, f"Article '{art.title}' updated successfully!")

        # DELETE ARTICLE
        elif action == 'delete_article':
            art_id = request.POST.get('article_id')
            art = Article.objects.filter(id=art_id).first()
            if art:
                a_title = art.title
                art.delete()
                messages.success(request, f"Article '{a_title}' was deleted.")

        # ================= JOB OFFERS CRUD =================
        elif action == 'update_job_status':
            offer_id = request.POST.get('offer_id')
            new_status = request.POST.get('status')
            offer = JobOffer.objects.filter(id=offer_id).first()
            if offer and new_status:
                offer.status = new_status
                offer.save()
                messages.success(request, f"Job Offer '{offer.job_title}' updated to '{offer.get_status_display()}'.")

        elif action == 'delete_job_offer':
            offer_id = request.POST.get('offer_id')
            offer = JobOffer.objects.filter(id=offer_id).first()
            if offer:
                offer.delete()
                messages.success(request, "Job offer record removed.")

        # ================= INQUIRIES CRUD =================
        elif action == 'toggle_message_read':
            msg_id = request.POST.get('message_id')
            msg = ContactMessage.objects.filter(id=msg_id).first()
            if msg:
                msg.is_read = not msg.is_read
                msg.save()
                state = "Read" if msg.is_read else "Unread"
                messages.success(request, f"Message marked as {state}.")

        elif action == 'delete_message':
            msg_id = request.POST.get('message_id')
            msg = ContactMessage.objects.filter(id=msg_id).first()
            if msg:
                msg.delete()
                messages.success(request, "Contact message deleted.")

        # ================= SITE SETTINGS CRUD =================
        elif action == 'update_settings':
            settings = SiteSettings.load()
            settings.owner_name = request.POST.get('owner_name', settings.owner_name).strip()
            settings.role_title = request.POST.get('role_title', settings.role_title).strip()
            settings.hero_headline = request.POST.get('hero_headline', settings.hero_headline).strip()
            settings.snapshot_text = request.POST.get('snapshot_text', settings.snapshot_text).strip()
            settings.email = request.POST.get('email', settings.email).strip()
            settings.location = request.POST.get('location', settings.location).strip()
            settings.github_url = request.POST.get('github_url', settings.github_url).strip()
            settings.linkedin_url = request.POST.get('linkedin_url', settings.linkedin_url).strip()
            settings.save()
            messages.success(request, "Site profile and public settings updated successfully!")

        return redirect('core:dashboard')


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
