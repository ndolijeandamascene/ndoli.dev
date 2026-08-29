import json
from datetime import datetime
from apps.core.models import SiteSettings

def seo_context(request):
    try:
        settings = SiteSettings.load()
    except Exception:
        settings = None

    owner_name = settings.owner_name if settings else 'NDOLI Jean Damascene'
    role_title = settings.role_title if settings else 'IT Professional · Software Developer · Systems Builder'
    github_url = settings.github_url if settings else 'https://github.com/ndolijeandamascene'
    linkedin_url = settings.linkedin_url if settings else 'https://linkedin.com/in/ndoli-jean-damascene'
    email = settings.email if settings else 'contact@ndoli.dev'

    person_schema = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": owner_name,
        "url": "https://ndoli.dev",
        "jobTitle": role_title,
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "Rwanda"
        },
        "alumniOf": {
            "@type": "CollegeOrUniversity",
            "name": "University of Rwanda"
        },
        "sameAs": [
            url for url in [github_url, linkedin_url] if url
        ],
        "knowsAbout": [
            "Software Engineering",
            "Python",
            "Django",
            "PostgreSQL",
            "Artificial Intelligence",
            "Retrieval-Augmented Generation",
            "pgvector",
            "Healthcare Information Systems",
            "Linux & Docker",
            "Computer Networking",
            "Cybersecurity"
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
        'PERSON_JSON_LD': json.dumps(person_schema),
    }
