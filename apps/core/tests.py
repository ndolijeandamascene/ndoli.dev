import json
import re
from django.test import TestCase, Client
from django.urls import reverse
from apps.core.models import SiteSettings, ContactMessage, Testimonial, JobOffer
from apps.projects.models import Category, Technology, Project
from apps.articles.models import ArticleCategory, Tag, Article
from apps.experience.models import Experience, Education, SkillCategory, Skill, Certification

class CompleteSEOAndPlatformTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Seed site settings
        self.settings = SiteSettings.load()
        self.settings.owner_name = 'NDOLI Jean Damascene'
        self.settings.role_title = 'IT Professional · Software Developer · Systems Builder'
        self.settings.phone_number = '+250 789 312 765'
        self.settings.whatsapp_url = 'https://wa.me/250789312765'
        self.settings.booking_url = 'https://cal.com/ndolijeandamascene'
        self.settings.save()

        # Seed test project category and project (IHKIP)
        self.category, _ = Category.objects.get_or_create(
            slug='healthcare-technology',
            defaults={'name': 'Healthcare Technology'}
        )
        self.tech_django, _ = Technology.objects.get_or_create(
            slug='django',
            defaults={'name': 'Django'}
        )
        self.tech_postgres, _ = Technology.objects.get_or_create(
            slug='postgresql',
            defaults={'name': 'PostgreSQL'}
        )
        self.project, _ = Project.objects.get_or_create(
            slug='ihkip',
            defaults={
                'title': 'IHKIP — Health Knowledge Intelligence Platform',
                'tagline': 'AI-assisted health knowledge intelligence platform',
                'category': self.category,
                'status': 'prototype',
                'featured': True,
                'is_published': True,
                'short_description': 'An AI-assisted health knowledge platform exploring clinical guidelines indexing and local pgvector search.',
                'overview': 'Overview of IHKIP architecture.',
                'problem_statement': 'Clinical guideline access challenges.',
                'solution_architecture': 'Django and pgvector local search pipeline.',
            }
        )
        self.project.technologies.add(self.tech_django, self.tech_postgres)

        # Seed article
        self.art_cat, _ = ArticleCategory.objects.get_or_create(
            slug='ai-systems',
            defaults={'name': 'AI & Systems'}
        )
        self.tag_rag, _ = Tag.objects.get_or_create(
            slug='rag',
            defaults={'name': 'RAG'}
        )
        self.article, _ = Article.objects.get_or_create(
            slug='building-local-rag-with-django',
            defaults={
                'title': 'Building a Local RAG Pipeline with Django and PostgreSQL',
                'excerpt': 'How to design a private RAG pipeline using Django and pgvector.',
                'content': '## Overview\n\nArticle content explaining local RAG.',
                'category': self.art_cat,
                'author_name': 'NDOLI Jean Damascene',
                'is_published': True,
            }
        )
        self.article.tags.add(self.tag_rag)

        # Seed experience
        self.exp, _ = Experience.objects.get_or_create(
            organization='GIRA LTD',
            role='ICT Officer',
            defaults={
                'start_date': 'June 2023',
                'end_date': 'Present',
                'is_current': True,
                'description': 'IT operations and systems management.',
                'responsibilities': 'Administer Linux servers\nManage network infrastructure',
            }
        )

        # Seed education
        self.edu, _ = Education.objects.get_or_create(
            institution='University of Rwanda',
            degree='Bachelor of Science with Honours in Information Technology',
            defaults={'graduation_year': '2022 – 2026'}
        )

        # Seed skills
        self.sc, _ = SkillCategory.objects.get_or_create(
            name='Software Development'
        )
        self.skill, _ = Skill.objects.get_or_create(
            category=self.sc,
            name='Django',
            defaults={'is_featured': True}
        )

    # 1. HOMEPAGE SEO TESTS
    def test_homepage_seo(self):
        res = self.client.get(reverse('core:home'))
        self.assertEqual(res.status_code, 200)

        # Title
        self.assertContains(res, '<title>NDOLI Jean Damascene | IT Professional & Software Developer</title>', html=False)
        
        # Meta description
        self.assertContains(res, 'name="description" content="NDOLI Jean Damascene is an IT professional and software developer from Rwanda building practical digital systems, intelligent software, and technology solutions."')
        
        # Canonical URL
        self.assertContains(res, '<link rel="canonical" href="https://ndoli.dev/">')
        
        # Language
        self.assertContains(res, '<html lang="en"')

        # H1 Check (Must contain NDOLI Jean Damascene)
        content = res.content.decode('utf-8')
        h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
        self.assertEqual(len(h1_matches), 1, "Homepage should contain exactly one <h1> tag")
        self.assertIn("NDOLI Jean Damascene", h1_matches[0])

        # Visible Content must identify NDOLI Jean Damascene & Role
        self.assertContains(res, "IT Professional &amp; Software Developer")

        # Open Graph & Twitter Cards
        self.assertContains(res, 'property="og:site_name" content="NDOLI"')
        self.assertContains(res, 'property="og:type" content="website"')
        self.assertContains(res, 'property="og:url" content="https://ndoli.dev/"')
        self.assertContains(res, 'property="og:image" content="https://ndoli.dev/static/images/ndoli-og-image.png"')
        self.assertContains(res, 'name="twitter:card" content="summary_large_image"')

        # Favicons & Manifest
        self.assertContains(res, 'href="/static/images/favicon.svg"')
        self.assertContains(res, 'href="/static/images/favicon-32x32.png"')
        self.assertContains(res, 'href="/static/images/apple-touch-icon.png"')
        self.assertContains(res, 'href="/static/site.webmanifest"')

        # Person & WebSite Schema
        self.assertContains(res, '"@type": "Person"')
        self.assertContains(res, '"@id": "https://ndoli.dev/#person"')
        self.assertContains(res, '"name": "NDOLI Jean Damascene"')
        self.assertContains(res, '"@type": "WebSite"')
        self.assertContains(res, '"@id": "https://ndoli.dev/#website"')

    # 2. ABOUT PAGE SEO TESTS
    def test_about_page_seo(self):
        res = self.client.get(reverse('core:about'))
        self.assertEqual(res.status_code, 200)

        # Title
        self.assertContains(res, '<title>About NDOLI Jean Damascene | IT Professional & Software Developer</title>')

        # H1
        content = res.content.decode('utf-8')
        h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
        self.assertEqual(len(h1_matches), 1)
        self.assertIn("About NDOLI Jean Damascene", h1_matches[0])

        # Canonical
        self.assertContains(res, '<link rel="canonical" href="https://ndoli.dev/about/">')

        # Schema: AboutPage + Breadcrumbs
        self.assertContains(res, '"@type": "AboutPage"')
        self.assertContains(res, '"@type": "BreadcrumbList"')
        self.assertContains(res, '"@id": "https://ndoli.dev/#person"')

        # Content verification
        self.assertContains(res, 'University of Rwanda')
        self.assertContains(res, 'Kigali, Rwanda')
        self.assertContains(res, 'Django')

    # 3. EXPERIENCE & SKILLS PAGE SEO TESTS
    def test_experience_and_skills_seo(self):
        # Experience List
        res_exp = self.client.get(reverse('experience:list'))
        self.assertEqual(res_exp.status_code, 200)
        self.assertContains(res_exp, '<title>NDOLI Jean Damascene — Professional Experience</title>')
        h1_exp = re.findall(r'<h1[^>]*>(.*?)</h1>', res_exp.content.decode('utf-8'), re.DOTALL)
        self.assertEqual(len(h1_exp), 1)
        self.assertIn("Professional Experience", h1_exp[0])
        self.assertContains(res_exp, 'NDOLI Jean Damascene')
        self.assertContains(res_exp, '"@type": "ProfilePage"')

        # Skills List
        res_skills = self.client.get(reverse('experience:skills'))
        self.assertEqual(res_skills.status_code, 200)
        self.assertContains(res_skills, '<title>Technical Skills | NDOLI Jean Damascene</title>')
        h1_skills = re.findall(r'<h1[^>]*>(.*?)</h1>', res_skills.content.decode('utf-8'), re.DOTALL)
        self.assertEqual(len(h1_skills), 1)
        self.assertIn("Technical Skills &amp; Stack", h1_skills[0])
        self.assertContains(res_skills, '"@type": "BreadcrumbList"')

    # 4. PROJECTS & CASE STUDY DETAIL SEO TESTS
    def test_projects_and_detail_seo(self):
        # Projects List
        res_list = self.client.get(reverse('projects:list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, '<title>Projects by NDOLI Jean Damascene | Software & Digital Systems</title>')
        h1_list = re.findall(r'<h1[^>]*>(.*?)</h1>', res_list.content.decode('utf-8'), re.DOTALL)
        self.assertEqual(len(h1_list), 1)
        self.assertIn("Projects", h1_list[0])
        self.assertContains(res_list, '"@type": "CollectionPage"')

        # Project Detail (IHKIP)
        res_detail = self.client.get(reverse('projects:detail', kwargs={'slug': 'ihkip'}))
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, '<title>IHKIP — Health Knowledge Intelligence Platform | NDOLI Jean Damascene</title>')
        self.assertContains(res_detail, '<link rel="canonical" href="https://ndoli.dev/projects/ihkip/">')
        self.assertContains(res_detail, '"@type": "SoftwareApplication"')
        self.assertContains(res_detail, '"@type": "BreadcrumbList"')
        self.assertContains(res_detail, 'NDOLI Jean Damascene')

    # 5. WRITING & ARTICLE DETAIL SEO TESTS
    def test_writing_and_article_detail_seo(self):
        # Writing List
        res_list = self.client.get(reverse('articles:list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, '<title>Writing by NDOLI Jean Damascene | Software, AI & Technology</title>')
        h1_list = re.findall(r'<h1[^>]*>(.*?)</h1>', res_list.content.decode('utf-8'), re.DOTALL)
        self.assertEqual(len(h1_list), 1)
        self.assertIn("Writing", h1_list[0])
        self.assertContains(res_list, '"@type": "CollectionPage"')

        # Article Detail
        res_detail = self.client.get(reverse('articles:detail', kwargs={'slug': 'building-local-rag-with-django'}))
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, '<title>Building a Local RAG Pipeline with Django and PostgreSQL | NDOLI Jean Damascene</title>')
        self.assertContains(res_detail, '<link rel="canonical" href="https://ndoli.dev/writing/building-local-rag-with-django/">')
        self.assertContains(res_detail, 'property="og:type" content="article"')
        self.assertContains(res_detail, '"@type": "TechArticle"')
        self.assertContains(res_detail, '"@type": "BreadcrumbList"')
        self.assertContains(res_detail, '"url": "https://ndoli.dev/about/"')
        self.assertContains(res_detail, 'NDOLI Jean Damascene')

    # 6. CV, CONTACT, NOW SEO TESTS
    def test_cv_contact_now_seo(self):
        # CV
        res_cv = self.client.get(reverse('core:cv'))
        self.assertEqual(res_cv.status_code, 200)
        self.assertContains(res_cv, '<title>NDOLI Jean Damascene — CV</title>')
        self.assertContains(res_cv, '<link rel="canonical" href="https://ndoli.dev/cv/">')
        self.assertContains(res_cv, '"@type": "ProfilePage"')
        self.assertContains(res_cv, 'Download PDF')

        # Contact
        res_contact = self.client.get(reverse('core:contact'))
        self.assertEqual(res_contact.status_code, 200)
        self.assertContains(res_contact, '<title>Contact NDOLI Jean Damascene</title>')
        self.assertContains(res_contact, '<link rel="canonical" href="https://ndoli.dev/contact/">')
        self.assertContains(res_contact, '"@type": "ContactPage"')

        # Now
        res_now = self.client.get(reverse('core:now'))
        self.assertEqual(res_now.status_code, 200)
        self.assertContains(res_now, '<title>Now | NDOLI Jean Damascene</title>')
        self.assertContains(res_now, '<link rel="canonical" href="https://ndoli.dev/now/">')

    # 7. AUTHOR CANONICAL REDIRECT TESTS
    def test_author_canonical_redirects(self):
        res = self.client.get('/author/ndoli-jean-damascene/')
        self.assertEqual(res.status_code, 301)
        self.assertEqual(res.url, '/about/')

        res2 = self.client.get('/author/')
        self.assertEqual(res2.status_code, 301)
        self.assertEqual(res2.url, '/about/')

    # 8. SITEMAP AND ROBOTS.TXT TESTS
    def test_sitemap_and_robots_txt(self):
        # Sitemap
        res_sitemap = self.client.get('/sitemap.xml')
        self.assertEqual(res_sitemap.status_code, 200)
        content_sitemap = res_sitemap.content.decode('utf-8')
        self.assertIn('<loc>https://ndoli.dev/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/about/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/projects/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/projects/ihkip/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/writing/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/writing/building-local-rag-with-django/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/experience/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/cv/</loc>', content_sitemap)
        self.assertIn('<loc>https://ndoli.dev/contact/</loc>', content_sitemap)
        
        # Excluded from sitemap
        self.assertNotIn('/admin/', content_sitemap)
        self.assertNotIn('/dashboard/', content_sitemap)
        self.assertNotIn('/login/', content_sitemap)

        # Robots.txt
        res_robots = self.client.get('/robots.txt')
        self.assertEqual(res_robots.status_code, 200)
        content_robots = res_robots.content.decode('utf-8')
        self.assertIn('User-agent: *', content_robots)
        self.assertIn('Allow: /', content_robots)
        self.assertIn('Disallow: /admin/', content_robots)
        self.assertIn('Disallow: /dashboard/', content_robots)
        self.assertIn('Disallow: /login/', content_robots)
        self.assertIn('Sitemap: https://ndoli.dev/sitemap.xml', content_robots)

    # 9. NOINDEX SECURITY AUDIT TESTS
    def test_noindex_rules(self):
        # Public pages must have index, follow
        res_home = self.client.get(reverse('core:home'))
        self.assertContains(res_home, '<meta name="robots" content="index, follow">')

        # Restricted pages must have noindex
        res_login = self.client.get(reverse('core:login'))
        self.assertContains(res_login, '<meta name="robots" content="noindex, nofollow">')

        res_404 = self.client.get('/non-existent-page-url-404/')
        self.assertContains(res_404, '<meta name="robots" content="noindex, follow">', status_code=404)

    # 10. FUNCTIONAL PLATFORM TESTS
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

        # 2. POST valid job offer
        response = self.client.post(reverse('core:hire'), {
            'company_name': 'Tech Enterprise Ltd',
            'contact_person': 'Jane Doe',
            'contact_email': 'hr@techenterprise.rw',
            'contact_phone': '+250788123456',
            'company_website': 'https://techenterprise.rw',
            'job_title': 'Lead Software Developer',
            'job_category': 'software_dev',
            'employment_type': 'fulltime_onsite',
            'work_location': 'Kigali, Rwanda',
            'offered_salary': '1,800,000 RWF / month',
            'salary_currency': 'RWF',
            'expected_start_date': 'Next 2 Weeks',
            'job_description': 'Building Django web systems and managing database architectures.',
            'website_url': '',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(JobOffer.objects.filter(company_name='Tech Enterprise Ltd').exists())

    def test_login_page_and_dashboard_access(self):
        from django.contrib.auth.models import User
        res_unauth = self.client.get(reverse('core:dashboard'))
        self.assertEqual(res_unauth.status_code, 302)

        res_login = self.client.get(reverse('core:login'))
        self.assertEqual(res_login.status_code, 200)
        self.assertContains(res_login, 'Admin Portal')

        User.objects.create_superuser(username='admin_ndoli', password='Password123!', email='admin@ndoli.dev')
        self.client.login(username='admin_ndoli', password='Password123!')

        res_dash = self.client.get(reverse('core:dashboard'))
        self.assertEqual(res_dash.status_code, 200)
        self.assertContains(res_dash, 'Website Control Dashboard')

        res_logout = self.client.get(reverse('core:logout'))
        self.assertEqual(res_logout.status_code, 302)

