from django.core.management.base import BaseCommand
from apps.core.models import SiteSettings
from apps.projects.models import Category, Technology, Project
from apps.articles.models import ArticleCategory, Tag, Article
from apps.experience.models import Experience, Education, SkillCategory, Skill, Certification

class Command(BaseCommand):
    help = 'Seeds database with verified live projects, CV, and specification data'

    def handle(self, *args, **options):
        self.stdout.write("Seeding database with verified live projects & CV data...")

        # 1. Site Settings
        settings = SiteSettings.load()
        settings.owner_name = 'NDOLI Jean Damascene'
        settings.short_brand = 'NDOLI'
        settings.role_title = 'IT Operations Administrator · Systems Administrator · Software Developer'
        settings.hero_headline = 'IT Operations Administrator, Systems Administrator, and Software Developer with over three years of experience supporting enterprise IT infrastructure, Linux and Windows environments, networking, and web platforms.'
        settings.snapshot_text = 'Experienced in providing Tier 2 technical support, administering Linux and Windows servers, managing enterprise networks, deploying cloud-hosted business applications, maintaining IT security standards, and supporting digital transformation initiatives.'
        settings.email = 'ndolijeandamascene@gmail.com'
        settings.location = 'Kigali, Rwanda'
        settings.github_url = 'https://github.com/ndolijeandamascene'
        settings.linkedin_url = 'https://linkedin.com/in/ndoli-jean-damascene'
        settings.save()
        self.stdout.write(self.style.SUCCESS("[OK] Site Settings updated"))

        # 2. Project Categories
        cat_health, _ = Category.objects.get_or_create(
            slug='healthcare-technology',
            defaults={'name': 'Healthcare Technology', 'description': 'Intelligent health knowledge systems, medical data governance, and clinical information pipelines.', 'order': 1}
        )
        cat_enterprise, _ = Category.objects.get_or_create(
            slug='enterprise-systems',
            defaults={'name': 'Enterprise & Business Systems', 'description': 'Corporate management platforms, internal operations software, and institutional systems.', 'order': 2}
        )
        cat_platforms, _ = Category.objects.get_or_create(
            slug='web-platforms',
            defaults={'name': 'Web Platforms & Digital Solutions', 'description': 'Discovery platforms, multi-tenant booking, and corporate public web systems.', 'order': 3}
        )
        cat_mobile, _ = Category.objects.get_or_create(
            slug='mobile-applications',
            defaults={'name': 'Mobile Applications', 'description': 'Android applications published on the Google Play Store.', 'order': 4}
        )

        # 3. Technologies
        tech_django, _ = Technology.objects.get_or_create(slug='django', defaults={'name': 'Django', 'category': 'backend'})
        tech_python, _ = Technology.objects.get_or_create(slug='python', defaults={'name': 'Python', 'category': 'language'})
        tech_csharp, _ = Technology.objects.get_or_create(slug='csharp', defaults={'name': 'C#', 'category': 'language'})
        tech_postgres, _ = Technology.objects.get_or_create(slug='postgresql', defaults={'name': 'PostgreSQL', 'category': 'database'})
        tech_mysql, _ = Technology.objects.get_or_create(slug='mysql', defaults={'name': 'MySQL', 'category': 'database'})
        tech_linux, _ = Technology.objects.get_or_create(slug='linux-server', defaults={'name': 'Linux Server', 'category': 'infrastructure'})
        tech_vps, _ = Technology.objects.get_or_create(slug='vps-cloud', defaults={'name': 'VPS / Cloud Hosting', 'category': 'infrastructure'})
        tech_networking, _ = Technology.objects.get_or_create(slug='networking-tcp-ip-dns', defaults={'name': 'Networking (TCP/IP, DNS)', 'category': 'security'})
        tech_ssl, _ = Technology.objects.get_or_create(slug='ssl-domain-management', defaults={'name': 'SSL & Domain Management', 'category': 'security'})
        tech_docker, _ = Technology.objects.get_or_create(slug='docker', defaults={'name': 'Docker', 'category': 'infrastructure'})
        tech_js, _ = Technology.objects.get_or_create(slug='javascript', defaults={'name': 'JavaScript', 'category': 'language'})
        tech_html_css, _ = Technology.objects.get_or_create(slug='html-css', defaults={'name': 'HTML5 & CSS3', 'category': 'language'})
        tech_android, _ = Technology.objects.get_or_create(slug='android-google-play', defaults={'name': 'Android / Google Play', 'category': 'other'})
        tech_pgvector, _ = Technology.objects.get_or_create(slug='pgvector', defaults={'name': 'pgvector', 'category': 'database'})
        tech_rag, _ = Technology.objects.get_or_create(slug='rag-architecture', defaults={'name': 'RAG Architecture', 'category': 'ai'})
        tech_qwen, _ = Technology.objects.get_or_create(slug='local-llm-qwen', defaults={'name': 'Local LLM (Qwen)', 'category': 'ai'})

        # 4. Verified Real Projects & Live URLs
        
        # 4.1 IHKIP (In Progress Flagship)
        ihkip, _ = Project.objects.update_or_create(
            slug='ihkip',
            defaults={
                'title': 'IHKIP — Intelligent Health Knowledge & Information Platform',
                'tagline': 'AI-assisted health knowledge intelligence platform exploring clinical guidelines indexing, semantic vector search, and local privacy-preserving LLM orchestration.',
                'category': cat_health,
                'status': 'prototype',
                'role': 'Lead Software Architect & AI Systems Developer',
                'featured': True,
                'order': 1,
                'is_published': True,
                'short_description': 'An intelligent health knowledge platform in active development, exploring how clinical guidelines can be indexed, retrieved via pgvector cosine distance, and governed with local models without third-party cloud leakage.',
                'overview': 'IHKIP is an ongoing research and engineering initiative exploring verifiable health knowledge retrieval. By organizing structured clinical guidance into high-dimensional vector embeddings, it enables rapid semantic search across medical documentation.',
                'problem_statement': 'Healthcare professionals and organizations frequently struggle to quickly query dense clinical guidelines. Cloud-hosted LLMs introduce severe data privacy concerns, while keyword search fails on synonyms and medical phrasing.',
                'solution_architecture': 'Structured ingestion pipeline chunking clinical guidance, indexing vector embeddings into PostgreSQL with pgvector, and orchestrating local quantized models (Qwen) with strict citation verification.',
                'implementation_details': 'Python/Django orchestration service, pgvector cosine distance queries, HNSW index optimization, and local inference server on Linux VPS.',
                'challenges_and_solutions': 'Mitigated clinical hallucinations by requiring all generated insights to cite exact source chunks and rejecting unsupported claims.',
                'security_and_governance': 'Self-hosted on Linux VPS with zero external API calls to safeguard health knowledge sovereignty.',
                'results_and_impact': 'Sub-second retrieval across comprehensive guidelines with grounded citation accuracy. Ongoing active prototype.',
                'lessons_learned': 'Relational databases augmented with vector extensions provide better transactional consistency than detached vector stores.',
                'future_roadmap': 'Multi-lingual clinical terminology indexing (Kinyarwanda & French) and automated guideline update diffs.',
                'repository_url': 'https://github.com/ndolijeandamascene',
            }
        )
        ihkip.technologies.set([tech_django, tech_postgres, tech_pgvector, tech_rag, tech_qwen, tech_python, tech_linux])

        # 4.2 GCIC Rwanda Platform (Live)
        gcic, _ = Project.objects.update_or_create(
            slug='gcic-rwanda',
            defaults={
                'title': 'GCIC Rwanda Enterprise Platform',
                'tagline': 'Official corporate web and institutional operations platform for GCIC Rwanda supporting enterprise systems, digital communications, and services.',
                'category': cat_enterprise,
                'status': 'production',
                'role': 'Software Developer & Systems Administrator',
                'featured': True,
                'order': 2,
                'is_published': True,
                'live_url': 'https://gcicrwanda.com/',
                'short_description': 'Official production platform for GCIC Rwanda, providing corporate information, service delivery workflows, and secure digital communications.',
                'overview': 'Designed, deployed, and administered in production to support GCIC Rwanda\'s institutional presence, corporate communications, and daily IT operational reliability.',
                'solution_architecture': 'Production web application deployed on high-performance cloud hosting with automated SSL, DNS routing, and database backups.',
                'implementation_details': 'Configured secure hosting, domain management, SSL termination, system monitoring, and ongoing preventive maintenance.',
                'results_and_impact': 'Live production platform serving GCIC Rwanda with high uptime, fast response times, and hardened security.',
                'repository_url': 'https://github.com/ndolijeandamascene',
            }
        )
        gcic.technologies.set([tech_django, tech_python, tech_postgres, tech_linux, tech_vps, tech_ssl, tech_networking])

        # 4.3 GlamourSearch (Live)
        glamour, _ = Project.objects.update_or_create(
            slug='glamoursearch',
            defaults={
                'title': 'GlamourSearch Web Platform',
                'tagline': 'Enterprise discovery, directory, and booking platform for personal care, beauty, and wellness businesses.',
                'category': cat_platforms,
                'status': 'production',
                'role': 'Full-Stack Developer & DevOps Administrator',
                'featured': True,
                'order': 3,
                'is_published': True,
                'live_url': 'https://glamoursearch.app/',
                'short_description': 'A live multi-vendor directory and appointment booking platform engineered for service discovery with customized booking management workflows.',
                'overview': 'Designed, built, and deployed to production at glamoursearch.app with complete DNS, SSL, database, and search optimization.',
                'solution_architecture': 'Full-stack application backed by relational database architecture with optimized multi-parameter search indexing and responsive mobile-first interfaces.',
                'implementation_details': 'Configured Linux VPS environment, automated SSL renewals, performance optimization, and scheduled database backups.',
                'results_and_impact': 'Live in production, simplifying client service discovery and appointment coordination.',
                'repository_url': 'https://github.com/ndolijeandamascene',
            }
        )
        glamour.technologies.set([tech_django, tech_python, tech_postgres, tech_linux, tech_vps, tech_ssl, tech_js, tech_html_css])

        # 4.4 GIRA Ltd Corporate Platform (Live)
        gira_corp, _ = Project.objects.update_or_create(
            slug='gira-corporate',
            defaults={
                'title': 'GIRA Ltd Corporate Platform',
                'tagline': 'Official corporate web platform for GIRA Ltd presenting company operations, investment services, and organizational profile.',
                'category': cat_enterprise,
                'status': 'production',
                'role': 'IT Manager & Systems Administrator',
                'featured': True,
                'order': 4,
                'is_published': True,
                'live_url': 'https://gira.rw/',
                'short_description': 'Corporate web platform representing GIRA Ltd, managing organizational branding, service presentation, and digital communications.',
                'overview': 'Maintained and administered under GIRA Ltd IT operations to provide corporate digital visibility and reliable web presence.',
                'solution_architecture': 'Cloud-hosted production environment with DNS configuration via AfriRegister, SSL encryption, and high uptime monitoring.',
                'implementation_details': 'Managed server deployment, domain routing, SSL certificate implementation, and disaster recovery procedures.',
                'results_and_impact': 'Established secure, official digital presence for GIRA Ltd.',
                'repository_url': 'https://github.com/ndolijeandamascene',
            }
        )
        gira_corp.technologies.set([tech_linux, tech_vps, tech_ssl, tech_networking, tech_python, tech_html_css])

        # 4.5 GIRA Enterprise Management System (Live Internal)
        gira_sys, _ = Project.objects.update_or_create(
            slug='gira-enterprise-system',
            defaults={
                'title': 'GIRA Enterprise Management System',
                'tagline': 'Internal enterprise resource, operations management, and administrative tracking platform for GIRA Ltd.',
                'category': cat_enterprise,
                'status': 'production',
                'role': 'IT Manager & Platform Developer',
                'featured': True,
                'order': 5,
                'is_published': True,
                'live_url': 'https://system.gira.rw/',
                'short_description': 'Secure internal business platform managing daily operational records, administrative workflows, and organizational asset tracking for GIRA Ltd.',
                'overview': 'Developed and administered to streamline internal corporate operations, user access controls, and administrative efficiency.',
                'solution_architecture': 'Hardened web platform with multi-tiered role-based authentication (RBAC), database transaction integrity, and sub-domain routing on system.gira.rw.',
                'implementation_details': 'Custom administrative dashboards, database backup policies, user activity audit trails, and network security controls.',
                'results_and_impact': 'Significantly improved operational coordination and data safety across company departments.',
                'repository_url': 'https://github.com/ndolijeandamascene',
            }
        )
        gira_sys.technologies.set([tech_django, tech_python, tech_postgres, tech_linux, tech_ssl, tech_networking])

        # 4.6 EcoMem Group Platform (Live)
        ecomem, _ = Project.objects.update_or_create(
            slug='ecomem-group',
            defaults={
                'title': 'EcoMem Group Digital Platform',
                'tagline': 'Corporate enterprise web platform for EcoMem Group showcasing sustainable initiatives, business operations, and partner engagements.',
                'category': cat_enterprise,
                'status': 'production',
                'role': 'Systems Administrator & Developer',
                'featured': False,
                'order': 6,
                'is_published': True,
                'live_url': 'https://www.ecomemgroup.com/',
                'short_description': 'Official digital platform for EcoMem Group, delivering corporate information, project portfolios, and partner communication channels.',
                'overview': 'Configured and deployed to provide a reliable, global web presence for EcoMem Group.',
                'solution_architecture': 'Production web hosting with domain management, SSL encryption, and responsive interface design.',
                'implementation_details': 'Handled DNS routing, server configuration, SSL deployment, and web content optimization.',
                'results_and_impact': 'Live production platform serving international partners and stakeholders.',
                'repository_url': 'https://github.com/ndolijeandamascene',
            }
        )
        ecomem.technologies.set([tech_linux, tech_ssl, tech_vps, tech_html_css, tech_js])

        self.stdout.write(self.style.SUCCESS("[OK] All 6 verified live projects & IHKIP in progress configured"))

        # 5. Articles
        art_cat_ai, _ = ArticleCategory.objects.get_or_create(
            slug='ai-intelligent-systems', defaults={'name': 'AI & Intelligent Systems', 'order': 1}
        )
        art_cat_devops, _ = ArticleCategory.objects.get_or_create(
            slug='devops-infrastructure', defaults={'name': 'DevOps & Infrastructure', 'order': 2}
        )

        tag_rag, _ = Tag.objects.get_or_create(slug='rag', defaults={'name': 'RAG'})
        tag_django, _ = Tag.objects.get_or_create(slug='django', defaults={'name': 'Django'})
        tag_postgres, _ = Tag.objects.get_or_create(slug='postgresql', defaults={'name': 'PostgreSQL'})
        tag_docker, _ = Tag.objects.get_or_create(slug='docker', defaults={'name': 'Docker'})
        tag_vps, _ = Tag.objects.get_or_create(slug='vps', defaults={'name': 'VPS'})
        tag_linux, _ = Tag.objects.get_or_create(slug='linux', defaults={'name': 'Linux'})

        art1, _ = Article.objects.update_or_create(
            slug='building-local-rag-with-django',
            defaults={
                'title': 'Building a Production-Oriented Local RAG Pipeline with Django and PostgreSQL',
                'excerpt': 'How to design and implement a private, high-performance retrieval-augmented generation pipeline using Django, pgvector, and local LLM orchestration.',
                'category': art_cat_ai,
                'reading_time_minutes': 7,
                'is_featured': True,
                'is_published': True,
                'content': """## Introduction

Retrieval-Augmented Generation (RAG) has emerged as one of the most practical applications of generative AI. By providing language models with contextual knowledge retrieved from a private, authoritative database, we eliminate hallucinations and ensure that outputs are verifiable.

While many tutorials rely on external cloud APIs and separate vector database services, building a **local, self-contained RAG pipeline** with **Django** and **PostgreSQL (pgvector)** offers immense advantages: total data privacy, simplified maintenance, zero per-query API costs, and seamless transactional integrity.

---

## 1. Why PostgreSQL with pgvector?

Instead of maintaining a separate standalone vector database alongside your relational application database, `pgvector` allows high-dimensional vector embeddings to live directly as a column type within your existing PostgreSQL tables.

### Key Benefits:
- **Transactional Consistency:** Vectors and relational data update atomically in the same database transaction.
- **Relational Filtering:** You can easily filter by category, date, or user permissions before or during vector distance calculations.
- **Operational Simplicity:** Only one database engine to back up, monitor, and scale.

---

## 2. Ingestion & Embedding Architecture

The retrieval pipeline consists of three core steps:

```
[Document / Guideline] 
       ↓ 
[Semantic Chunking (500 tokens + 50 overlap)] 
       ↓ 
[Local Embedding Model (e.g., all-MiniLM-L6-v2)] 
       ↓ 
[PostgreSQL Vector Column (vector(384))]
```

---

## 3. Querying & Orchestrating with Local LLMs

When a user submits a query:
1. Generate the query vector embedding.
2. Execute a cosine distance query using `pgvector` operators (`<=>` for cosine distance):

```sql
SELECT title, content_chunk, 1 - (embedding <=> :query_vector) AS similarity
FROM knowledge_chunks
WHERE is_active = TRUE
ORDER BY embedding <=> :query_vector
LIMIT 5;
```

3. Construct the prompt with retrieved context chunks and pass it to your local **Qwen** or **Llama** model running on a local inference server.

---

## Conclusion & Key Takeaway

For healthcare, legal, and enterprise use cases in Rwanda and beyond, local RAG architectures provide the highest standard of data sovereignty, predictable performance, and verifiable knowledge governance.
"""
            }
        )
        art1.tags.set([tag_rag, tag_django, tag_postgres])
        art1.related_projects.set([ihkip])

        art2, _ = Article.objects.update_or_create(
            slug='deploying-django-on-vps',
            defaults={
                'title': 'Deploying Production Django Applications on a Linux VPS with Docker and Nginx',
                'excerpt': 'A step-by-step architectural guide to deploying hardened, containerized Django applications with reverse proxies, automatic SSL, and zero downtime.',
                'category': art_cat_devops,
                'reading_time_minutes': 6,
                'is_featured': True,
                'is_published': True,
                'content': """## Overview

Deploying a production Django application to a dedicated Linux VPS requires careful consideration of security headers, reverse proxy configuration, static file delivery, and database isolation.

In this guide, we explore the standard deployment pattern used for `ndoli.dev` and institutional client applications.

---

## The Production Stack

```
Internet (HTTPS 443)
       │
       ▼
Reverse Proxy (Nginx / EasyPanel) [Handles SSL, Rate Limiting & Gzip]
       │
       ▼ (Internal Network)
Gunicorn WSGI Server (Running Django 5.x)
       │
       ├──► WhiteNoise (Static Assets)
       └──► PostgreSQL Database
```

---

## Key Production Hardening Rules

1. **Never run with `DEBUG=True` in production.**
2. **Use WhiteNoise for static files** with `CompressedManifestStaticFilesStorage`.
3. **Configure strict HTTP headers:** HSTS, X-Frame-Options, and Content-Security-Policy.
4. **Isolate secrets** strictly through environment variables.
"""
            }
        )
        art2.tags.set([tag_docker, tag_django, tag_vps, tag_linux])

        self.stdout.write(self.style.SUCCESS("[OK] Technical articles verified"))

        # 6. Work Experience (Strictly from CV)
        Experience.objects.all().delete()

        Experience.objects.create(
            organization='GCIC Ltd',
            role='ICT Officer',
            location='Kigali, Rwanda',
            employment_type='Full-time',
            start_date='January 2025',
            end_date='Present',
            is_current=True,
            description='Supporting daily enterprise IT operations, network infrastructure, and business applications across multiple departments.',
            responsibilities='Support daily IT operations by maintaining enterprise systems, network infrastructure, and business applications.\nAdminister hosting environments, monitor server performance, and provide technical assistance to staff across multiple departments.\nCoordinate deployment of new software solutions, manage system upgrades, and maintain IT asset records.\nSupport cybersecurity initiatives through system monitoring and preventive maintenance.\nTroubleshoot infrastructure, connectivity, and application issues while ensuring reliable technology services and accurate operational documentation.',
            technologies_used='Enterprise Systems, Network Infrastructure, Server Administration, Cybersecurity, IT Asset Management',
            order=1,
        )

        Experience.objects.create(
            organization='GIRA Ltd',
            role='ICT Officer',
            location='Kigali, Rwanda',
            employment_type='Full-time',
            start_date='June 2023',
            end_date='Present',
            is_current=True,
            description='Delivering Tier 2 technical support, administering Linux servers and VPS infrastructure, and coordinating application deployments.',
            responsibilities='Provide technical support for employees by diagnosing and resolving hardware, software, networking, and system-related issues while ensuring minimal disruption to business operations.\nAdminister Linux servers, VPS infrastructure, and cloud-hosted services supporting enterprise web applications.\nInstall, configure, and maintain operating systems, applications, and ICT equipment while monitoring system performance and implementing preventive maintenance.\nManage backups, server security, DNS configuration, SSL certificates, and hosting environments to ensure business continuity and service reliability.\nCoordinate deployment of internally developed business applications and collaborate with development teams to support production environments.\nDeliver user training and technical guidance while maintaining ICT documentation and promoting compliance with organizational security policies.',
            technologies_used='Linux Server, VPS Infrastructure, DNS, SSL Certificates, Backup & Disaster Recovery, User Training',
            order=2,
        )

        Experience.objects.create(
            organization='CPC Ltd',
            role='IT Manager',
            location='Rwanda',
            employment_type='Full-time',
            start_date='May 2024',
            end_date='September 2024',
            is_current=False,
            description='Led daily corporate IT operations, overseeing infrastructure, server administration, and technology solution implementations.',
            responsibilities='Led the organization\'s daily IT operations by overseeing ICT infrastructure, server administration, network services, and user support activities.\nManaged implementation of technology solutions, coordinated system deployments, and maintained backup and disaster recovery procedures.\nEnsured the availability and security of business systems while working closely with management to improve operational efficiency through technology.',
            technologies_used='ICT Infrastructure, Server Administration, Network Services, Backup & Recovery, Strategic IT Planning',
            order=3,
        )

        Experience.objects.create(
            organization='Urumuri Rw\'Icyizere Ltd',
            role='IT Support',
            location='Rwanda',
            employment_type='Full-time',
            start_date='September 2023',
            end_date='March 2024',
            is_current=False,
            description='Managed internal IT infrastructure, web application hosting, and network system uptime.',
            responsibilities='Managed internal IT infrastructure and website hosting services.\nProvided support for web-based applications and hosting environments.\nMaintained network systems and ensured system uptime.',
            technologies_used='IT Infrastructure, Website Hosting, Web Applications Support, Network Systems',
            order=4,
        )

        Experience.objects.create(
            organization='ES Sumba',
            role='IT Officer',
            location='Rwanda',
            employment_type='Full-time',
            start_date='June 2021',
            end_date='May 2023',
            is_current=False,
            description='Managed institutional ICT infrastructure, computers, servers, network equipment, and digital learning platforms.',
            responsibilities='Managed the school\'s ICT infrastructure by maintaining computers, servers, network equipment, and internet connectivity while providing technical support to staff and students.\nInstalled and configured software, performed preventive maintenance, and supported digital learning platforms.\nMaintained ICT equipment records and delivered technical training to improve users\' digital skills and effective use of technology resources.',
            technologies_used='Computers & Servers, Networking, Digital Learning Platforms, Hardware Maintenance',
            order=5,
        )

        Experience.objects.create(
            organization='Codadev Training Program',
            role='Technical Trainer',
            location='Rwanda',
            employment_type='Contract',
            start_date='2022',
            end_date='2023',
            is_current=False,
            description='Delivered hands-on technical instruction in application troubleshooting, Heroku/VPS deployment, and debugging.',
            responsibilities='Trained on technical instruction and training delivery methods.\nProvided training on application troubleshooting and Heroku deployment environments.\nMentored developers on debugging and deployment practices.',
            technologies_used='Technical Instruction, Heroku, Deployment Workflows, Debugging, Mentorship',
            order=6,
        )

        self.stdout.write(self.style.SUCCESS("[OK] Work Experience updated with all 6 verified positions from CV"))

        # 7. Education
        Education.objects.all().delete()
        Education.objects.create(
            institution='University of Rwanda',
            degree='Bachelor of Science with Honours in Information Technology',
            field_of_study='Information Technology',
            graduation_year='2022 – 2026',
            description='Comprehensive Honours degree covering Software Engineering, Relational Database Theory, Computer Networks, Systems Analysis, and Cybersecurity.',
            is_visible=True,
            order=1,
        )
        Education.objects.create(
            institution='Secondary Education',
            degree='Advanced Level (A2), Mathematics, Computer Science & Economics',
            field_of_study='Mathematics, Computer Science & Economics',
            graduation_year='2018 – 2021',
            description='Strong academic foundation in algorithmic problem solving, computational mathematics, and economic systems.',
            is_visible=True,
            order=2,
        )
        self.stdout.write(self.style.SUCCESS("[OK] Education updated (BSc with Honours in IT, Advanced Level A2)"))

        # 8. Certifications
        Certification.objects.all().delete()
        certs = [
            ('NDG Linux Essentials', 'NDG / Cisco Networking Academy', '2023'),
            ('Linux Unhatched', 'Cisco Networking Academy', '2023'),
            ('IT Essentials', 'Cisco Networking Academy', '2023'),
            ('Cybersecurity Administration', 'Cisco Networking Academy', '2024'),
            ('Network Defense', 'Cisco Networking Academy', '2024'),
            ('Firewalls & Cloud Security', 'Cisco Networking Academy', '2024'),
            ('OS & Endpoint Security', 'Cisco Networking Academy', '2024'),
            ('Ethical Hacker', 'Cisco Networking Academy', '2024'),
            ('Responsive Web Design', 'freeCodeCamp', '2023'),
            ('Foundational C# with Microsoft', 'Microsoft & freeCodeCamp', '2024'),
        ]
        for idx, (c_name, c_org, c_date) in enumerate(certs, 1):
            Certification.objects.create(
                name=c_name,
                issuing_organization=c_org,
                issue_date=c_date,
                is_verified=True,
                order=idx,
            )
        self.stdout.write(self.style.SUCCESS("[OK] Certifications updated (10 verified technical certifications)"))

        # 9. Skill Categories & Skills from CV
        SkillCategory.objects.all().delete()
        skill_cats = [
            ('Systems & Server Administration', [
                ('Linux & Windows Server', 'Core', True),
                ('VPS / Cloud Hosting (Contabo, Hostinger, cPanel)', 'Core', True),
                ('Backup & Disaster Recovery', 'Core', True),
                ('SSL & Domain Management (AfriRegister)', 'Core', True),
            ]),
            ('Software & Web Development', [
                ('Django', 'Core Framework', True),
                ('Python', 'Core', True),
                ('C#', 'Framework & Language', True),
                ('PostgreSQL / MySQL', 'Core Database', True),
                ('HTML5, CSS3, JavaScript', 'Web Frontend', True),
                ('Android / Google Play Store Publishing', 'Mobile', False),
            ]),
            ('Networking & Cybersecurity', [
                ('Networking (TCP/IP, DNS, Routing)', 'Core', True),
                ('Cybersecurity Practices & Hardening', 'Security', True),
                ('Firewalls & Cloud Security', 'Defense', True),
                ('OS & Endpoint Security', 'Defense', True),
                ('Ethical Hacking Fundamentals', 'Security', False),
            ]),
        ]

        for cat_idx, (cat_name, skills) in enumerate(skill_cats, 1):
            sc = SkillCategory.objects.create(name=cat_name, order=cat_idx)
            for s_idx, (s_name, level, feat) in enumerate(skills, 1):
                Skill.objects.create(
                    category=sc, name=s_name, level_tag=level, is_featured=feat, order=s_idx
                )

        self.stdout.write(self.style.SUCCESS("[OK] Skills taxonomy matrix updated"))
        self.stdout.write(self.style.SUCCESS("All verified live projects & CV data successfully loaded!"))
