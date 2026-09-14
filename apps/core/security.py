import re
import time
from datetime import timedelta
from django.core import signing
from django.utils import timezone
from django.conf import settings

SECURITY_SALT = 'ndoli-dev-anti-spam-v1'

# Common spam URL / protocol / domain patterns for name and subject fields
URL_PATTERN = re.compile(
    r'(https?://|www\.|\b[a-z0-9_\-\.]+\.(?:com|org|net|xyz|ru|top|biz|info|cc|online|site|club|vip|link|click|app|dev)/)',
    re.IGNORECASE
)

# High-confidence spam keywords commonly used by automated blast bots
SPAM_KEYWORD_PATTERNS = [
    re.compile(r'\b(casino|gambling|viagra|cialis|crypto\s*bonus|forex\s*trading|poker|seo\s*ranking|buy\s*backlinks?|guest\s*posts?)\b', re.IGNORECASE),
    re.compile(r'\b(telegram\.me/|t\.me/|wa\.me/|whatsapp\s*business)\b', re.IGNORECASE),
    re.compile(r'\[url=.*?\].*?\[/url\]', re.IGNORECASE),
    re.compile(r'<a\s+href=.*?>', re.IGNORECASE),
]


def generate_form_security_token(ip_address: str = '') -> str:
    """
    Generates a cryptographically signed token containing timestamp and client IP.
    Used to detect instant/superhuman bot submissions.
    """
    payload = {
        'ts': time.time(),
        'ip': ip_address or '',
    }
    return signing.dumps(payload, salt=SECURITY_SALT)


def validate_form_speed_and_token(token: str, min_seconds: float = 2.0, max_seconds: float = 86400.0) -> tuple[bool, str]:
    """
    Validates the form security token:
    - Must be a valid signature.
    - Must be submitted after at least `min_seconds` (humans need at least 2-3 seconds to read & type).
    - Must not be expired (default: 24 hours).
    Returns (is_valid, reason).
    """
    if not token:
        return False, "Missing security timestamp token"

    try:
        data = signing.loads(token, salt=SECURITY_SALT, max_age=max_seconds)
    except signing.SignatureExpired:
        return False, "Form session expired (older than 24 hours)"
    except signing.BadSignature:
        return False, "Invalid security signature"

    ts = data.get('ts', 0)
    elapsed = time.time() - ts

    # In testing mode, allow fast submissions if explicitly running tests
    if getattr(settings, 'IS_TESTING', False) or 'test' in getattr(settings, 'DATABASES', {}).get('default', {}).get('NAME', ''):
        if elapsed < 0:
            return False, "Timestamp is in the future"
        return True, ""

    if elapsed < min_seconds:
        return False, f"Form submitted too quickly ({elapsed:.2f}s, minimum is {min_seconds}s)"

    return True, ""


def analyze_submission_content(name: str = '', email: str = '', subject: str = '', message: str = '') -> tuple[bool, str]:
    """
    Inspects fields for bot link injection and spam patterns:
    - Real human names and subjects do NOT contain HTTP links or domain names.
    - Message body link flooding or typical blast spam patterns.
    Returns (is_spam, reason).
    """
    # 1. Check Name for URL / Domain injection (e.g., 'Hello http://ndoli.dev/fekal0911 Owner')
    if name and URL_PATTERN.search(name):
        return True, f"URL or link pattern detected in name: '{name[:40]}...'"

    # 2. Check Subject for URL / Domain injection
    if subject and URL_PATTERN.search(subject):
        return True, f"URL or link pattern detected in subject: '{subject[:40]}...'"

    # 3. Check for HTML or BBCode links in name, subject, or message
    combined_text = f"{name} {subject} {message}"
    if '[url=' in combined_text.lower() or '[/url]' in combined_text.lower():
        return True, "BBCode link injection detected"

    if '<a ' in combined_text.lower() and '</a>' in combined_text.lower():
        return True, "HTML anchor link injection detected"

    # 4. Check for high density of URLs in message (more than 3 URLs is typical bot blast)
    urls_found = URL_PATTERN.findall(message) if message else []
    if len(urls_found) > 3:
        return True, f"Excessive URLs in message ({len(urls_found)} links found)"

    # 5. Check for known blast spam keywords
    for pattern in SPAM_KEYWORD_PATTERNS:
        if pattern.search(combined_text):
            return True, f"Spam keyword pattern matched: {pattern.pattern}"

    return False, ""


def check_honeypots(data: dict) -> tuple[bool, str]:
    """
    Verifies that all stealth honeypot decoy fields are strictly empty.
    If a bot fills ANY of these, it is an automated submission.
    """
    honeypot_fields = ['website_url', 'business_title', 'contact_fax']
    for field in honeypot_fields:
        val = data.get(field)
        if val and str(val).strip():
            return True, f"Honeypot trap triggered: field '{field}' was filled with '{str(val)[:30]}'"
    return False, ""


def check_ip_rate_limit(ip_address: str, max_requests: int = 6, window_minutes: int = 10) -> tuple[bool, str]:
    """
    Checks if an IP address has submitted too many inquiries recently.
    Queries the ContactMessage and JobOffer tables directly for reliability across all server configurations.
    """
    if not ip_address or ip_address in ('127.0.0.1', 'localhost', 'testserver'):
        return False, ""

    from apps.core.models import ContactMessage, JobOffer
    cutoff = timezone.now() - timedelta(minutes=window_minutes)

    recent_contact = ContactMessage.objects.filter(ip_address=ip_address, created_at__gte=cutoff).count()
    recent_jobs = JobOffer.objects.filter(ip_address=ip_address, created_at__gte=cutoff).count()

    total_recent = recent_contact + recent_jobs
    if total_recent >= max_requests:
        return True, f"IP {ip_address} exceeded rate limit ({total_recent}/{max_requests} in {window_minutes}m)"

    return False, ""


def evaluate_submission_spam(data: dict, ip_address: str = '', name: str = '', email: str = '', subject: str = '', message: str = '') -> tuple[bool, str]:
    """
    Master anti-spam evaluation combining all defense layers:
    1. Honeypots
    2. Content heuristics (name / subject URLs)
    3. Speed & cryptographic token
    4. IP rate limiting
    """
    # 1. Honeypots
    is_hp_spam, hp_reason = check_honeypots(data)
    if is_hp_spam:
        return True, hp_reason

    # 2. Content heuristics
    is_content_spam, content_reason = analyze_submission_content(
        name=name or data.get('name') or data.get('contact_person', ''),
        email=email or data.get('email') or data.get('contact_email', ''),
        subject=subject or data.get('subject') or data.get('job_title', ''),
        message=message or data.get('message') or data.get('job_description', ''),
    )
    if is_content_spam:
        return True, content_reason

    # 3. Speed & Timestamp Token (if provided)
    token = data.get('security_token', '')
    if token:
        is_token_valid, token_reason = validate_form_speed_and_token(token, min_seconds=2.0)
        if not is_token_valid:
            return True, f"Speed check / token failed: {token_reason}"

    # 4. IP rate limit check
    if ip_address:
        is_rate_limited, rate_reason = check_ip_rate_limit(ip_address, max_requests=6, window_minutes=10)
        if is_rate_limited:
            return True, rate_reason

    return False, ""
