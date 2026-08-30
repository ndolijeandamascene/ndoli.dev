import os
import json
from pathlib import Path
from datetime import datetime
from django.conf import settings as django_settings
from apps.core.models import SiteSettings

def seo_context(request):
    # Hot-reload .env in development so changes are instantly reflected
    if getattr(django_settings, 'DEBUG', False):
        try:
            env_path = django_settings.BASE_DIR / '.env'
            if env_path.exists():
                with open(env_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith('#') and '=' in line:
                            k, v = line.split('=', 1)
                            os.environ[k.strip()] = v.strip().strip('"\'')
        except Exception:
            pass

    try:
        settings = SiteSettings.load()
    except Exception:
        settings = None

    owner_name = os.environ.get('OWNER_NAME') or (settings.owner_name if settings else 'NDOLI Jean Damascene')
    role_title = os.environ.get('ROLE_TITLE') or (settings.role_title if settings else 'IT Professional · Software Developer · Systems Builder')
    github_url = os.environ.get('GITHUB_URL') or (settings.github_url if settings else 'https://github.com/ndolijeandamascene')
    linkedin_url = os.environ.get('LINKEDIN_URL', '').strip() or (settings.linkedin_url.strip() if settings and settings.linkedin_url else '')
    email = os.environ.get('OWNER_EMAIL') or os.environ.get('DEFAULT_FROM_EMAIL') or (settings.email if settings else 'ndolijeandamascene@gmail.com')
    phone_number = os.environ.get('OWNER_PHONE') or os.environ.get('PHONE_NUMBER') or (settings.phone_number if settings else '+250 789 312 765')
    whatsapp_url = os.environ.get('WHATSAPP_URL') or (settings.whatsapp_url if settings else f'https://wa.me/{phone_number.replace(" ", "").replace("+", "")}')
    booking_url = os.environ.get('BOOKING_URL') or (settings.booking_url if settings else 'https://cal.com/ndolijeandamascene')
    availability_badge = os.environ.get('AVAILABILITY_BADGE') or (settings.availability_badge if settings else 'Available for Technical Systems & Engineering')
    years_of_experience = os.environ.get('YEARS_OF_EXPERIENCE') or (settings.years_of_experience if settings else '3+ Years')

    same_as_links = [github_url] if github_url else []
    if linkedin_url:
        same_as_links.append(linkedin_url)

    global_schema_graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Person",
                "@id": "https://ndoli.dev/#person",
                "name": "NDOLI Jean Damascene",
                "givenName": "Jean Damascene",
                "familyName": "NDOLI",
                "url": "https://ndoli.dev/",
                "image": "https://ndoli.dev/static/images/ndoli-og-image.png",
                "jobTitle": "IT Professional & Software Developer",
                "description": "IT professional and software developer from Rwanda building practical digital systems, intelligent software, and technology solutions.",
                "nationality": {
                    "@type": "Country",
                    "name": "Rwanda"
                },
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Kigali",
                    "addressCountry": "Rwanda"
                },
                "alumniOf": {
                    "@type": "CollegeOrUniversity",
                    "name": "University of Rwanda"
                },
                "sameAs": same_as_links,
                "knowsAbout": [
                    "Software Development",
                    "Information Technology",
                    "Django",
                    "Python",
                    "PostgreSQL",
                    "Artificial Intelligence",
                    "RAG",
                    "pgvector",
                    "Software Architecture",
                    "Digital Systems",
                    "Linux Server Administration",
                    "Computer Networking",
                    "Cybersecurity"
                ]
            },
            {
                "@type": "WebSite",
                "@id": "https://ndoli.dev/#website",
                "url": "https://ndoli.dev/",
                "name": "NDOLI",
                "alternateName": "ndoli.dev",
                "description": "Personal website of NDOLI Jean Damascene",
                "publisher": {
                    "@id": "https://ndoli.dev/#person"
                },
                "inLanguage": "en"
            }
        ]
    }

    return {
        'site_settings': settings,
        'CANONICAL_HOST': 'https://ndoli.dev',
        'CURRENT_YEAR': datetime.now().year,
        'OWNER_NAME': owner_name,
        'ROLE_TITLE': role_title,
        'GITHUB_URL': github_url,
        'LINKEDIN_URL': linkedin_url,
        'EMAIL': email,
        'PHONE_NUMBER': phone_number,
        'WHATSAPP_URL': whatsapp_url,
        'BOOKING_URL': booking_url,
        'AVAILABILITY_BADGE': availability_badge,
        'YEARS_OF_EXPERIENCE': years_of_experience,
        'PERSON_JSON_LD': json.dumps(global_schema_graph, indent=2),
    }
