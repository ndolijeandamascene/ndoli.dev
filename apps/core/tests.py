from django.test import TestCase, Client
from django.urls import reverse
from apps.core.models import SiteSettings, ContactMessage
from apps.projects.models import Category, Technology, Project
from apps.articles.models import ArticleCategory, Tag, Article
from apps.experience.models import Experience, Education, SkillCategory, Skill

class PlatformTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Seed minimal test data with get_or_create to ensure idempotency
        self.settings = SiteSettings.load()
        self.category, _ = Category.objects.get_or_create(
            slug='healthcare-technology',
            defaults={'name': 'Healthcare Technology'}
        )
        self.tech, _ = Technology.objects.get_or_create(
            slug='django',
            defaults={'name': 'Django'}
        )
        self.project, _ = Project.objects.get_or_create(
            slug='ihkip',
            defaults={
                'title': 'IHKIP — Intelligent Health Knowledge & Information Platform',
                'tagline': 'AI health knowledge platform',
                'category': self.category,
                'status': 'prototype',
                'featured': True,
                'is_published': True,
                'short_description': 'Test short description',
                'overview': 'Test overview',
                'solution_architecture': 'Architecture and data flow design.',
            }
        )
        self.project.technologies.add(self.tech)

        self.art_cat, _ = ArticleCategory.objects.get_or_create(
            slug='ai-systems',
            defaults={'name': 'AI & Systems'}
        )
        self.article, _ = Article.objects.get_or_create(
            slug='building-local-rag-with-django',
            defaults={
                'title': 'Building a Local RAG System with Django and PostgreSQL',
                'excerpt': 'Test excerpt for article',
                'content': '## Heading 2\n\nArticle body test with `code`.',
                'category': self.art_cat,
                'is_published': True,
            }
        )

        self.exp, _ = Experience.objects.get_or_create(
            organization='GIRA LTD',
            role='IT Manager',
            defaults={
                'start_date': 'June 2023',
                'end_date': 'Present',
                'is_current': True,
                'description': 'IT operations and systems management.',
                'responsibilities': 'Lead IT systems\nManage networks',
            }
        )

        self.edu, _ = Education.objects.get_or_create(
            institution='University of Rwanda',
            degree='Bachelor of Science in Information Technology',
            defaults={'graduation_year': '2026'}
        )

        self.sc, _ = SkillCategory.objects.get_or_create(
            name='Programming Languages'
        )
        self.skill, _ = Skill.objects.get_or_create(
            category=self.sc,
            name='Python',
            defaults={'is_featured': True}
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NDOLI Jean Damascene')
        self.assertContains(response, 'IHKIP')
        self.assertContains(response, 'application/ld+json')

    def test_about_page_loads(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'University of Rwanda')

    def test_projects_list_and_detail(self):
        res_list = self.client.get(reverse('projects:list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, 'IHKIP')

        res_detail = self.client.get(reverse('projects:detail', kwargs={'slug': 'ihkip'}))
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, 'IHKIP')
        self.assertContains(res_detail, 'AI health knowledge platform')

    def test_articles_list_and_detail(self):
        res_list = self.client.get(reverse('articles:list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, 'Building a Local RAG System')

        res_detail = self.client.get(reverse('articles:detail', kwargs={'slug': 'building-local-rag-with-django'}))
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, 'Heading 2')

    def test_experience_and_skills_pages(self):
        res_exp = self.client.get(reverse('experience:list'))
        self.assertEqual(res_exp.status_code, 200)
        self.assertContains(res_exp, 'GIRA LTD')

        res_skills = self.client.get(reverse('experience:skills'))
        self.assertEqual(res_skills.status_code, 200)
        self.assertContains(res_skills, 'Python')

    def test_cv_and_now_pages(self):
        res_cv = self.client.get(reverse('core:cv'))
        self.assertEqual(res_cv.status_code, 200)
        self.assertContains(res_cv, 'NDOLI JEAN DAMASCENE')

        res_now = self.client.get(reverse('core:now'))
        self.assertEqual(res_now.status_code, 200)
        self.assertContains(res_now, 'What I\'m Doing Now')

    def test_contact_form_submission(self):
        response = self.client.post(reverse('core:contact'), {
            'name': 'Inquirer Name',
            'email': 'inquiry@example.com',
            'subject': 'Collaboration Opportunity',
            'message': 'We would like to discuss a software project.',
            'website_url': '',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(email='inquiry@example.com').exists())

    def test_contact_honeypot_rejects_bots(self):
        response = self.client.post(reverse('core:contact'), {
            'name': 'Spam Bot',
            'email': 'bot@spam.com',
            'subject': 'Buy something',
            'message': 'Spam message content',
            'website_url': 'http://spam-link.com',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactMessage.objects.filter(email='bot@spam.com').exists())

    def test_hire_me_page_and_form_submission(self):
        # 1. GET page
        res_get = self.client.get(reverse('core:hire'))
        self.assertEqual(res_get.status_code, 200)
        self.assertContains(res_get, 'Hire NDOLI Jean Damascene')

        # 2. POST valid job offer with salary
        from apps.core.models import JobOffer
        response = self.client.post(reverse('core:hire'), {
            'company_name': 'Tech Enterprise Ltd',
            'contact_person': 'Jane Doe',
            'contact_email': 'hr@techenterprise.rw',
            'contact_phone': '+250788123456',
            'company_website': 'https://techenterprise.rw',
            'job_title': 'Lead IT Operations Administrator',
            'job_category': 'it_operations',
            'employment_type': 'fulltime_onsite',
            'work_location': 'Kigali, Rwanda',
            'offered_salary': '1,800,000 RWF / month',
            'salary_currency': 'RWF',
            'expected_start_date': 'Next 2 Weeks',
            'job_description': 'Overseeing enterprise systems and managing Linux infrastructure.',
            'website_url': '',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(JobOffer.objects.filter(company_name='Tech Enterprise Ltd').exists())

    def test_login_page_and_dashboard_access(self):
        from django.contrib.auth.models import User
        # 1. Unauthenticated request to dashboard redirects to login
        res_unauth = self.client.get(reverse('core:dashboard'))
        self.assertEqual(res_unauth.status_code, 302)

        # 2. Login page loads
        res_login = self.client.get(reverse('core:login'))
        self.assertEqual(res_login.status_code, 200)
        self.assertContains(res_login, 'Admin Portal')

        # 3. Create test admin and authenticate
        User.objects.create_superuser(username='admin_ndoli', password='Password123!', email='admin@ndoli.dev')
        self.client.login(username='admin_ndoli', password='Password123!')

        # 4. Authenticated request opens dashboard
        res_dash = self.client.get(reverse('core:dashboard'))
        self.assertEqual(res_dash.status_code, 200)
        self.assertContains(res_dash, 'Website Control Dashboard')
        self.assertContains(res_dash, 'LIVE CONTROL CENTER')

        # 5. Logout
        res_logout = self.client.get(reverse('core:logout'))
        self.assertEqual(res_logout.status_code, 302)

    def test_seo_sitemap_and_robots(self):
        res_sitemap = self.client.get('/sitemap.xml')
        self.assertEqual(res_sitemap.status_code, 200)
        self.assertContains(res_sitemap, '<loc>')

        res_robots = self.client.get('/robots.txt')
        self.assertEqual(res_robots.status_code, 200)
        self.assertContains(res_robots, 'Sitemap: https://ndoli.dev/sitemap.xml')
