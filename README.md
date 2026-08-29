# NDOLI.DEV

## Personal Technology Platform

**Official Domain:** `https://ndoli.dev`
**Owner:** NDOLI Jean Damascene
**Platform Type:** Personal professional website, portfolio, research hub, project showcase, and technology publication platform
**Primary Purpose:** Establish NDOLI Jean Damascene as a credible technology professional and builder while creating a long-term digital home for projects, research, engineering work, writing, and professional opportunities.

---

# 1. MASTER IMPLEMENTATION INSTRUCTION

> **THIS README IS THE AUTHORITATIVE PRODUCT, DESIGN, CONTENT, ARCHITECTURE, AND IMPLEMENTATION SPECIFICATION FOR NDOLI.DEV.**

The coding AI must read and understand this entire document before implementing the project.

The coding AI must:

1. Treat this README as the primary source of truth.
2. Implement the requirements in this document rather than creating a generic portfolio template.
3. Preserve the long-term architecture described here.
4. Avoid unnecessary technologies, dependencies, abstractions, or complexity.
5. Prefer maintainable, secure, performant solutions.
6. Build reusable components rather than hard-coding individual pages.
7. Make the website content-driven and manageable through Django Admin.
8. Never invent personal achievements, statistics, clients, partnerships, certifications, publications, awards, or professional claims.
9. Never publish placeholder content as if it were factual.
10. Clearly mark content requiring owner confirmation.
11. Keep the website extensible for future projects, research, companies, products, and publications.
12. Implement the project in phases.
13. Test each major feature before moving to the next phase.
14. Do not remove requirements simply because they require additional work.
15. If a requirement conflicts with another requirement, prioritize:

* Security
* Accessibility
* Performance
* SEO correctness
* Maintainability
* User experience

16. Do not introduce React, Next.js, Vue, or other frontend frameworks unless there is a documented technical reason.
17. Do not use fake testimonials, fake metrics, fake reviews, fake client logos, or fake social proof.
18. Do not create SEO spam pages.
19. Do not overuse animations.
20. The final product must feel like a serious technology professional's website, not a generic developer template.

---

# 2. PRODUCT VISION

NDOLI.DEV is the long-term digital identity of NDOLI Jean Damascene.

The website must communicate:

> **I build technology that solves real-world problems.**

The platform should demonstrate that NDOLI is not simply someone listing technical skills, but someone who:

* builds software;
* designs systems;
* experiments with AI;
* works with real-world technology problems;
* researches solutions;
* develops digital platforms;
* documents technical work;
* learns continuously;
* contributes to technology;
* turns ideas into working systems.

The website must therefore prioritize **evidence of work over claims of expertise**.

---

# 3. BRAND POSITIONING

## Primary identity

**NDOLI Jean Damascene**

## Professional positioning

**IT Professional · Software Engineer · Technology Builder**

Alternative wording may be used where appropriate:

**Software Developer · AI Systems Builder · IT Professional**

Do not claim titles that have not been verified.

---

# 4. BRAND MESSAGE

Primary statement:

> **I build technology that solves real-world problems.**

Supporting statement:

> I'm NDOLI Jean Damascene, an IT professional and software engineer focused on building intelligent systems, digital platforms, and practical technology solutions.

The website should communicate the following ideas:

* Build.
* Solve.
* Research.
* Learn.
* Document.
* Improve.
* Innovate.

Avoid excessive marketing language.

---

# 5. TARGET AUDIENCE

The website must serve several audiences.

## 5.1 Employers

People evaluating NDOLI for:

* software engineering;
* IT roles;
* system development;
* AI/software roles;
* technical leadership;
* technology projects.

They need to quickly understand:

* who NDOLI is;
* technical capabilities;
* experience;
* projects;
* education;
* evidence of work;
* contact information.

---

## 5.2 Technology professionals

Developers, engineers, architects, researchers, and technical communities.

They need:

* technical project details;
* architecture;
* GitHub;
* research;
* articles;
* engineering decisions;
* lessons learned.

---

## 5.3 Institutions and organizations

Potential:

* institutional partners;
* government organizations;
* healthcare organizations;
* technology organizations;
* universities;
* innovation organizations;
* NGOs;
* research partners.

They need to understand:

* what NDOLI builds;
* the real-world problems being addressed;
* project maturity;
* technical capability;
* research interests;
* professional contact information.

---

## 5.4 Potential clients

Organizations looking for:

* software development;
* system development;
* websites;
* digital platforms;
* AI solutions;
* IT solutions.

Do not turn the website into a generic freelance marketplace.

---

## 5.5 Researchers and students

They should be able to discover:

* technical articles;
* research;
* project architecture;
* experiments;
* open-source work;
* lessons learned.

---

# 6. CORE WEBSITE PRINCIPLE

The site should answer five questions within seconds:

1. **Who is NDOLI?**
2. **What does NDOLI build?**
3. **What has NDOLI built?**
4. **What does NDOLI know/research?**
5. **How can someone contact NDOLI?**

---

# 7. INFORMATION ARCHITECTURE

Primary navigation:

```text
Home
About
Projects
Research
Articles
Open Source
Experience
Contact
```

Secondary navigation:

```text
Resume
GitHub
```

The navigation must remain simple.

Do not create a huge navigation menu.

---

# 8. URL STRUCTURE

Primary domain:

```text
https://ndoli.dev/
```

Canonical domain:

```text
ndoli.dev
```

If `www.ndoli.dev` exists, it should redirect to:

```text
https://ndoli.dev/
```

Recommended routes:

```text
/
/about/
/projects/
/projects/<slug>/
/research/
/research/<slug>/
/articles/
/articles/<slug>/
/opensource/
/experience/
/resume/
/contact/
/search/
/privacy/
/terms/
/404/
```

Optional future routes:

```text
/certifications/
/education/
/speaking/
/media/
/uses/
/now/
```

Only create these when meaningful content exists.

---

# 9. HOMEPAGE

The homepage is the most important page.

It must communicate the identity of NDOLI immediately.

## 9.1 Hero section

Display:

**NDOLI Jean Damascene**

Then:

> **I build technology that solves real-world problems.**

Supporting text:

> IT professional and software engineer building intelligent systems, digital platforms, and practical technology solutions.

Primary CTA:

**Explore my work**

Secondary CTA:

**View résumé**

Additional optional CTA:

**Contact me**

---

# 10. HERO DESIGN

The hero must be visually strong but restrained.

Avoid:

* excessive gradients;
* floating 3D objects;
* generic AI brain graphics;
* stock photos;
* excessive particle effects;
* meaningless animations.

Preferred visual direction:

* premium;
* modern;
* technical;
* clean;
* editorial;
* confident;
* minimal;
* responsive.

Possible visual elements:

* subtle grid;
* code-inspired details;
* technical diagrams;
* project preview;
* subtle motion;
* carefully selected photography if available.

---

# 11. PERSONAL INTRODUCTION

After the hero, provide a concise introduction.

Example:

> I'm a technology professional focused on building software systems that turn ideas and real-world problems into practical digital solutions.

This section must link to `/about/`.

---

# 12. FEATURED PROJECT

The homepage must feature the strongest current project.

Initial featured project:

## IHKIP

**Intelligent Health Knowledge & Information Platform**

The project should be presented as the flagship project without making the entire personal website exclusively about healthcare.

Display:

* project name;
* concise description;
* problem;
* solution;
* technology;
* project status;
* link to case study.

CTA:

**Explore IHKIP**

---

# 13. PROJECTS SECTION

Homepage should show selected projects.

Each project card should support:

* title;
* short description;
* category;
* technologies;
* status;
* image/screenshot;
* project type;
* links.

Possible project categories:

```text
Software
AI
Healthcare Technology
Web Platform
Enterprise Systems
Infrastructure
Research
Open Source
Experimental
```

Do not show technologies as meaningless badges everywhere.

---

# 14. PROJECT DETAIL PAGE

Every major project should have a case-study page.

Structure:

```text
Project Hero
↓
Overview
↓
Problem
↓
Context
↓
Objectives
↓
Solution
↓
Architecture
↓
Technology
↓
Implementation
↓
Challenges
↓
Engineering Decisions
↓
Results
↓
Lessons Learned
↓
Screenshots
↓
Future Roadmap
↓
Related Projects
↓
Contact CTA
```

Only display sections when actual information exists.

---

# 15. IHKIP CASE STUDY

IHKIP should be presented professionally.

Name:

**IHKIP — Intelligent Health Knowledge & Information Platform**

Description:

> An AI-assisted health knowledge intelligence platform designed around authoritative clinical knowledge, retrieval, governance, learning, and responsible AI.

The case study may discuss:

* clinical knowledge;
* knowledge governance;
* RAG;
* vector search;
* PostgreSQL/pgvector;
* local AI;
* Qwen orchestration;
* clinical engines;
* learning;
* analytics;
* security;
* architecture.

Never imply official government ownership, endorsement, deployment, or partnership unless explicitly verified.

Use wording such as:

> “A project developed to explore...”

or

> “The platform is designed to...”

when institutional status has not been formally confirmed.

---

# 16. PROJECT DATA MODEL

Create a reusable `Project` model.

Suggested fields:

```text
title
slug
short_description
description
problem
solution
context
project_type
status
featured
hero_image
thumbnail
technologies
repository_url
live_url
documentation_url
start_date
end_date
results
lessons_learned
future_roadmap
created_at
updated_at
published_at
is_published
seo_title
seo_description
canonical_url
```

Technologies should preferably be represented through a reusable model or structured relationship rather than an unstructured text field.

---

# 17. PROJECT STATUS

Supported statuses:

```text
Concept
Prototype
In Development
Active
Completed
Archived
```

Do not use exaggerated statuses such as:

```text
Revolutionary
World-Class
Industry-Leading
```

---

# 18. ABOUT PAGE

The About page should be more detailed than the homepage.

Sections:

```text
Introduction
Professional Identity
What I Build
Technical Focus
Experience
Education
Professional Philosophy
Current Interests
Selected Projects
Contact
```

The page should tell a coherent professional story.

---

# 19. PROFESSIONAL STORY

The story should focus on progression:

```text
Learning
↓
Building
↓
Professional Experience
↓
System Development
↓
AI / Intelligent Systems
↓
Research & Innovation
↓
Future Direction
```

Do not invent a dramatic personal story.

Use factual information only.

---

# 20. EXPERIENCE PAGE

Create a structured experience timeline.

Each experience record:

```text
organization
role
location
employment_type
start_date
end_date
description
responsibilities
technologies
achievements
is_current
```

Display:

* organization;
* role;
* dates;
* responsibilities;
* selected achievements;
* technologies where relevant.

Achievements must be factual.

---

# 21. EDUCATION

Create an Education model.

Fields:

```text
institution
degree
field
start_date
end_date
description
grade
is_visible
```

Current known professional education should be entered only after verification from the owner's supplied information.

Do not invent academic grades.

---

# 22. SKILLS

Skills should be grouped.

Suggested categories:

```text
Software Engineering
Backend Development
Frontend Development
Databases
AI & Machine Learning
DevOps & Infrastructure
Cybersecurity
Networking
Tools
```

Known technologies may include:

```text
Python
Django
PostgreSQL
JavaScript
HTML
CSS
Git
Docker
Redis
pgvector
REST APIs
Linux
```

Only list technologies the owner actually uses or has confirmed.

Avoid percentage skill bars.

Do not display:

```text
Python 95%
Django 92%
```

These are subjective and provide little evidence.

---

# 23. RESEARCH SECTION

Create `/research/`.

Purpose:

Show technical investigation, experimentation, and deeper thinking.

Research topics may include:

* AI systems;
* RAG;
* healthcare technology;
* local LLM deployment;
* knowledge intelligence;
* software architecture;
* digital transformation;
* information systems;
* responsible AI.

Each research entry should support:

```text
title
slug
abstract
problem
research_question
methodology
findings
limitations
references
related_projects
publication_date
status
```

---

# 24. ARTICLES

Create a publishing system.

URL:

```text
/articles/
```

Article categories:

```text
Software Engineering
AI
Healthcare Technology
DevOps
Cybersecurity
Systems
Research
Career
Technology
```

Article model:

```text
title
slug
excerpt
content
author
category
cover_image
tags
published_at
updated_at
reading_time
is_featured
is_published
seo_title
seo_description
canonical_url
```

Articles must support:

* Markdown or rich content;
* headings;
* code blocks;
* syntax highlighting;
* images;
* links;
* citations;
* related articles.

---

# 25. ARTICLE QUALITY

Articles must prioritize useful knowledge.

Avoid publishing articles purely to target keywords.

Good:

> Building a production-oriented RAG pipeline with PostgreSQL and pgvector

Bad:

> Best AI RAG PostgreSQL Rwanda AI RAG Platform 2026

Do not keyword-stuff.

---

# 26. OPEN SOURCE

Create `/opensource/`.

Display:

* GitHub profile;
* selected repositories;
* open-source contributions;
* technical projects.

Each repository may show:

```text
name
description
language
stars
forks
repository_url
topics
```

If GitHub API integration is used, cache API results and handle rate limits.

Never make the website dependent on GitHub being available.

---

# 27. GITHUB INTEGRATION

Use GitHub as a supporting professional identity.

The website should link to the owner's GitHub profile.

Do not expose private repositories.

Do not claim contributions that cannot be verified.

Optional future functionality:

```text
GitHub repository cards
Recent public activity
Selected repositories
Contribution summary
```

---

# 28. RESUME

Create:

```text
/resume/
```

The page should provide:

* professional summary;
* experience;
* education;
* skills;
* selected projects;
* certifications;
* contact.

Provide a downloadable PDF when the final CV is available.

Do not generate a résumé automatically from incomplete data without owner approval.

---

# 29. CONTACT

Create `/contact/`.

Include:

* professional email;
* GitHub;
* other verified professional profiles;
* optional contact form.

Contact form fields:

```text
name
email
subject
message
```

Optional:

```text
organization
purpose
```

Do not collect unnecessary personal data.

---

# 30. CONTACT FORM SECURITY

Implement:

* CSRF protection;
* server-side validation;
* rate limiting;
* spam protection;
* email validation;
* message length limits;
* logging of security events;
* safe email handling.

Never expose SMTP credentials.

Use environment variables.

---

# 31. SOCIAL LINKS

Only display verified profiles.

Potential links:

```text
GitHub
LinkedIn
X
Email
```

If a platform becomes unavailable, remove or update the link.

Do not invent social accounts.

---

# 32. PERSONAL BRAND ENTITY

The website should clearly establish:

```text
NDOLI Jean Damascene
        │
        ├── ndoli.dev
        │
        ├── Projects
        │
        ├── Research
        │
        ├── Articles
        │
        └── Open Source
```

The website should clearly associate major projects with the owner.

For example:

> IHKIP is a project developed by NDOLI Jean Damascene.

Only use such statements when factually accurate.

---

# 33. SEO STRATEGY

SEO is a core requirement.

The website must be optimized for:

```text
NDOLI Jean Damascene
NDOLI
NDOLI software developer
NDOLI Rwanda
IHKIP
IHKIP Rwanda
Rwanda healthcare AI
Rwanda software developer
Rwanda AI systems
```

Do not create pages solely for keywords.

---

# 34. SEO FOUNDATIONS

Every indexable page must support:

```text
<title>
<meta name="description">
canonical URL
robots metadata
Open Graph
Twitter/X metadata
structured data where appropriate
```

Use unique titles and descriptions.

---

# 35. CANONICAL DOMAIN

Canonical domain:

```text
https://ndoli.dev
```

Do not mix:

```text
http://ndoli.dev
https://www.ndoli.dev
https://ndoli.dev
```

The production canonical version must be:

```text
https://ndoli.dev
```

If `www.ndoli.dev` exists:

```text
www.ndoli.dev → 301 → ndoli.dev
```

---

# 36. XML SITEMAP

Generate:

```text
/sitemap.xml
```

Include only canonical, indexable, published URLs.

Do not include:

```text
/admin/
private pages
draft articles
login pages
search results
duplicate URLs
```

---

# 37. ROBOTS.TXT

Create:

```text
/robots.txt
```

Allow public content.

Disallow private/admin areas.

Example concept:

```text
User-agent: *
Allow: /

Disallow: /admin/
Disallow: /account/
Disallow: /private/

Sitemap: https://ndoli.dev/sitemap.xml
```

Adapt to actual application routes.

---

# 38. STRUCTURED DATA

Implement Schema.org structured data where appropriate.

Potential schemas:

```text
Person
WebSite
WebPage
BreadcrumbList
Article
BlogPosting
SoftwareApplication
CreativeWork
Organization
```

Do not create structured data for entities that do not exist.

---

# 39. PERSON SCHEMA

The personal website should contain appropriate Person structured data.

Conceptual structure:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "NDOLI Jean Damascene",
  "url": "https://ndoli.dev"
}
```

Add verified URLs such as GitHub through `sameAs`.

Do not include unverified information.

---

# 40. PROJECT STRUCTURED DATA

For software projects, use an appropriate Schema.org type.

Potentially:

```text
SoftwareApplication
CreativeWork
WebApplication
```

Choose based on the actual project.

Do not incorrectly label every project as a commercial product.

---

# 41. ARTICLE STRUCTURED DATA

Articles should support:

```text
headline
description
author
datePublished
dateModified
image
mainEntityOfPage
```

All data must match visible content.

---

# 42. BREADCRUMBS

Implement breadcrumb structured data where useful.

Example:

```text
Home
→ Projects
→ IHKIP
```

Breadcrumbs should be visible where they improve navigation.

---

# 43. GOOGLE SEARCH CONSOLE

The deployment documentation must include instructions for:

1. Adding `ndoli.dev` to Google Search Console.
2. Verifying domain ownership.
3. Submitting `sitemap.xml`.
4. Testing URLs.
5. Monitoring indexing.
6. Monitoring search performance.
7. Monitoring Core Web Vitals.
8. Monitoring indexing issues.

Do not promise rankings.

---

# 44. GOOGLE VISIBILITY STRATEGY

The site should build a strong relationship between:

```text
NDOLI Jean Damascene
↓
ndoli.dev
↓
Projects
↓
IHKIP
↓
Research
↓
Articles
↓
GitHub
```

External references may include:

* GitHub;
* university pages;
* conference pages;
* research repositories;
* technical publications;
* legitimate institutional references.

Never create fake backlinks.

Never buy spam backlinks.

---

# 45. PERFORMANCE

Performance is a first-class requirement.

Targets:

```text
Lighthouse Performance: >= 90
Lighthouse Accessibility: >= 95
Lighthouse Best Practices: >= 95
Lighthouse SEO: >= 95
```

These are targets, not guaranteed values.

Optimize:

* images;
* fonts;
* CSS;
* JavaScript;
* database queries;
* caching;
* HTML;
* API requests.

---

# 46. FRONTEND PRINCIPLES

Prefer:

```text
semantic HTML
modern CSS
minimal JavaScript
progressive enhancement
responsive design
accessible components
```

Avoid unnecessary frontend frameworks.

---

# 47. RESPONSIVE DESIGN

The website must work on:

```text
Mobile
Tablet
Laptop
Desktop
Large screens
```

Test at common breakpoints.

Do not simply shrink desktop content.

Design mobile intentionally.

---

# 48. ACCESSIBILITY

Target WCAG 2.2 AA principles where practical.

Requirements:

* keyboard navigation;
* visible focus states;
* semantic HTML;
* accessible forms;
* proper labels;
* sufficient contrast;
* meaningful alt text;
* reduced-motion support;
* logical heading hierarchy;
* accessible navigation;
* accessible modal/dialog behavior.

Respect:

```css
prefers-reduced-motion
```

---

# 49. DESIGN SYSTEM

Create a reusable design system.

Define:

```text
colors
typography
spacing
radius
shadows
borders
buttons
cards
badges
forms
navigation
sections
containers
```

Do not scatter arbitrary values throughout templates.

Use CSS variables or a coherent token system.

---

# 50. VISUAL STYLE

Desired style:

**Premium + Technical + Editorial + Minimal**

Characteristics:

* strong typography;
* generous whitespace;
* clear hierarchy;
* restrained color palette;
* subtle technical details;
* high-quality project imagery;
* polished interactions.

Avoid:

* generic SaaS template appearance;
* excessive neon;
* excessive gradients;
* huge animated backgrounds;
* stock developer illustrations;
* unnecessary 3D;
* excessive glassmorphism.

---

# 51. DARK MODE

Support:

```text
Light
Dark
System
```

Persist user preference.

Avoid flashing between themes during page load.

Ensure contrast works in both modes.

---

# 52. TYPOGRAPHY

Typography should communicate professionalism.

Recommended hierarchy:

```text
H1 — strong, distinctive
H2 — section heading
H3 — subsection
Body — highly readable
Small — metadata
```

Do not use too many fonts.

Prefer one primary font family and optionally one secondary accent family.

Optimize font loading.

---

# 53. ANIMATIONS

Animations should support usability.

Good:

* page transitions;
* subtle reveal;
* hover interactions;
* navigation transitions;
* project card interactions.

Avoid:

* constant movement;
* distracting particles;
* excessive scrolling effects;
* animations that delay content.

Support reduced motion.

---

# 54. IMAGES

Use optimized images.

Preferred formats:

```text
AVIF
WebP
JPEG
PNG when appropriate
```

Implement:

* responsive images;
* width/height attributes;
* lazy loading where appropriate;
* descriptive alt text;
* image compression.

Do not use copyrighted images without permission.

---

# 55. IMAGE PLACEHOLDERS

During development, clearly label placeholders.

Never allow:

```text
placeholder-image.jpg
```

to appear as a final professional asset.

Admin should make it easy to replace assets.

---

# 56. TECHNOLOGY STACK

Recommended stack:

```text
Backend:
Django

Database:
PostgreSQL

Frontend:
Django Templates
HTML5
CSS3
JavaScript

Optional:
Alpine.js

Deployment:
Docker
EasyPanel
VPS

Version Control:
GitHub

CI/CD:
GitHub Actions
```

Use Redis only if required.

Do not add infrastructure without purpose.

---

# 57. DJANGO ARCHITECTURE

Prefer modular Django apps.

Suggested structure:

```text
config/
core/
pages/
projects/
experience/
education/
research/
articles/
opensource/
contact/
seo/
```

Optional:

```text
analytics/
accounts/
media/
```

Only create apps where they provide clear separation.

---

# 58. DJANGO PRINCIPLES

Follow:

* Django best practices;
* reusable templates;
* class-based views where appropriate;
* clear services;
* forms;
* validators;
* permissions;
* database constraints;
* indexes;
* migrations;
* tests.

Avoid putting large business logic directly in views.

---

# 59. DATABASE

Use PostgreSQL in production.

Use appropriate indexes.

Use:

* unique slugs;
* timestamps;
* publication states;
* relationships;
* constraints.

Avoid storing everything in JSON unless there is a clear reason.

---

# 60. CONTENT MANAGEMENT

The site must be manageable through Django Admin.

Admin should support:

```text
Projects
Articles
Research
Experience
Education
Skills
Certifications
Achievements
Publications
Social Links
Site Settings
Media
```

---

# 61. ADMIN UX

Django Admin should be customized professionally.

Provide:

* list filters;
* search;
* ordering;
* fieldsets;
* slug prepopulation;
* publication controls;
* image previews where useful;
* date filters;
* relationship management.

Admin is an internal tool and does not need to match the public website design.

---

# 62. CONTENT WORKFLOW

Content should support:

```text
Draft
Review
Published
Archived
```

The owner should be able to prepare content without immediately publishing it.

---

# 63. SITE SETTINGS

Create a central site settings model.

Potential fields:

```text
site_name
site_description
owner_name
owner_title
email
location
github_url
linkedin_url
x_url
default_og_image
favicon
logo
resume_file
analytics_enabled
```

Do not put secrets here.

---

# 64. SEO SETTINGS

Allow admin management of:

```text
SEO title
SEO description
canonical URL
Open Graph image
robots behavior
```

But generate sensible defaults automatically.

---

# 65. SEARCH

Create an internal site search.

Search:

```text
Projects
Articles
Research
```

Do not index private/admin content.

Use PostgreSQL full-text search if appropriate.

Do not introduce Elasticsearch unless the site genuinely requires it.

---

# 66. 404 PAGE

Create a polished 404 page.

It should say:

> This page doesn't exist.

Provide:

```text
Back home
Explore projects
Search
```

Do not expose server errors.

---

# 67. ERROR HANDLING

Production must not expose:

* Django debug pages;
* stack traces;
* database errors;
* environment variables;
* internal paths.

Configure:

```text
DEBUG=False
```

in production.

---

# 68. SECURITY

Implement:

* HTTPS;
* secure cookies;
* CSRF protection;
* XSS protection;
* clickjacking protection;
* HSTS where appropriate;
* Content Security Policy where practical;
* secure headers;
* rate limiting;
* secure file uploads;
* admin protection;
* secret management.

---

# 69. SECRETS

Never commit:

```text
.env
API keys
SMTP passwords
database passwords
secret keys
private credentials
```

Use environment variables.

Provide:

```text
.env.example
```

with safe placeholders.

---

# 70. FILE UPLOAD SECURITY

For CVs, project images, and articles:

* validate extensions;
* validate MIME types;
* limit file sizes;
* sanitize filenames;
* prevent executable uploads;
* use secure storage paths.

---

# 71. DATABASE BACKUPS

Deployment documentation must describe:

* PostgreSQL backups;
* retention;
* restoration;
* backup verification.

Do not assume a backup exists simply because the server provider has snapshots.

---

# 72. MONITORING

Production should support error monitoring.

Possible integration:

```text
Honeybadger
```

or another appropriate service.

Monitoring must not expose private data.

---

# 73. ANALYTICS

Use privacy-conscious analytics.

Possible option:

```text
Simple Analytics
```

or another privacy-friendly solution.

Track useful events such as:

```text
Project viewed
Resume downloaded
Contact submitted
Article viewed
GitHub clicked
```

Do not collect unnecessary personal information.

---

# 74. COOKIE POLICY

Avoid unnecessary cookies.

If analytics does not require consent under the applicable implementation/legal model, document the reasoning.

If cookies requiring consent are introduced, implement a proper consent mechanism.

Do not install advertising trackers by default.

---

# 75. EMAIL

Email configuration must use environment variables.

Example:

```text
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL
```

Never hard-code credentials.

---

# 76. VPS DEPLOYMENT

The production website will run on the owner's existing VPS.

Current VPS:

```text
62.171.182.99
```

Do not expose this IP publicly in website source code or frontend content unless operationally necessary.

Domain:

```text
ndoli.dev
```

Production:

```text
https://ndoli.dev
```

---

# 77. EASY PANEL

Deployment should be compatible with EasyPanel.

The application should be containerized.

Suggested architecture:

```text
Internet
   ↓
DNS
   ↓
EasyPanel
   ↓
HTTPS
   ↓
Django application
   ↓
PostgreSQL
```

Add Redis only if required.

---

# 78. DOCKER

Use a production-ready Dockerfile.

Requirements:

* non-root container where practical;
* deterministic dependencies;
* environment configuration;
* health checks;
* static file handling;
* proper logging;
* production WSGI/ASGI server.

Do not use:

```text
python manage.py runserver
```

in production.

---

# 79. STATIC FILES

Use a proper static-file strategy.

Django:

```text
collectstatic
```

Use compression/minification where beneficial.

---

# 80. MEDIA

Media files should be handled separately from static assets.

Current architecture can use local VPS storage.

Do not introduce S3 unless there is a future need.

---

# 81. DATABASE CONNECTION

Production PostgreSQL credentials must come from environment variables.

Use connection pooling if useful.

Do not open PostgreSQL publicly to the internet unnecessarily.

---

# 82. GITHUB REPOSITORY

Recommended repository:

```text
ndoli-dev
```

Repository description:

> Personal technology platform and professional website for NDOLI Jean Damascene.

The repository should contain:

```text
README.md
LICENSE
.gitignore
.env.example
Dockerfile
docker-compose.yml or deployment configuration
requirements.txt / pyproject.toml
src/
tests/
docs/
```

---

# 83. README HIERARCHY

This README is the master specification.

Additional documentation may be created:

```text
docs/
├── architecture.md
├── deployment.md
├── seo.md
├── content.md
├── design-system.md
└── operations.md
```

Additional documents must not contradict this README.

---

# 84. GIT WORKFLOW

Recommended branches:

```text
main
develop
feature/*
fix/*
```

Use meaningful commits.

Examples:

```text
feat: add project case study system
feat: implement article publishing
fix: correct canonical URL generation
perf: optimize project images
security: harden contact form
```

---

# 85. CI/CD

GitHub Actions should eventually run:

```text
lint
tests
security checks
build
```

Production deployment may be automated after validation.

Never deploy broken code automatically.

---

# 86. TESTING

Minimum testing areas:

```text
Models
Views
Forms
URLs
Admin
SEO
Sitemap
Robots
Contact form
Search
Authentication if applicable
Permissions
Project pages
Article pages
```

---

# 87. SEO TESTING

Automated tests should verify:

* every public page has a title;
* important pages have meta descriptions;
* canonical URLs are correct;
* sitemap exists;
* robots exists;
* no accidental `noindex`;
* Open Graph metadata exists;
* structured data is valid where expected.

---

# 88. SECURITY TESTING

Test:

* CSRF;
* authentication;
* authorization;
* upload validation;
* form abuse;
* rate limiting;
* XSS;
* SQL injection;
* security headers;
* production DEBUG setting.

---

# 89. ACCESSIBILITY TESTING

Test:

* keyboard navigation;
* focus;
* forms;
* heading hierarchy;
* contrast;
* mobile navigation;
* screen-reader labels;
* reduced motion.

---

# 90. PERFORMANCE TESTING

Test:

```text
Homepage
Project detail
Article detail
Research detail
Contact
```

Check:

* page size;
* number of requests;
* image size;
* JavaScript;
* CSS;
* database queries;
* Core Web Vitals.

---

# 91. CONTENT RULES

Content must be:

* truthful;
* professional;
* clear;
* concise;
* technically meaningful;
* evidence-oriented.

Avoid:

> passionate developer

unless used naturally.

Avoid:

> expert in everything

Avoid:

> revolutionary platform

unless supported by evidence.

---

# 92. CLAIM VALIDATION

Before publishing:

```text
Is this true?
Can it be supported?
Is the wording accurate?
Does it exaggerate?
```

If uncertain, use neutral wording.

---

# 93. PROFESSIONAL PHOTOGRAPHY

If the owner provides a professional portrait, it may be used in:

* About;
* homepage;
* Open Graph;
* résumé;
* author profile.

Do not generate or use a fake portrait.

---

# 94. PERSONAL BRAND COLORS

The visual identity should incorporate the owner's preferred color palette: **Green, Yellow, and combined Green & Yellow (Lime / Chartreuse / Duo-tone Gradients)**, balanced with clean, restrained neutral tones.

### Preferred Color Direction:

```text
Base & Backgrounds:
- Dark Mode: Deep neutral / near-black / rich charcoal (#0B0F10, #12181A)
- Light Mode: Crisp white / soft warm neutral (#FAFAFA, #F4F6F5)

Primary Accent (Green):
- Emerald / Tech Green (e.g., #10B981, #059669, #00D084)
- Communicates precision, systems engineering, vitality, and stability.

Secondary Accent (Yellow):
- Warm Amber / Golden Yellow (e.g., #F59E0B, #EAB308, #FFD166)
- Communicates energy, intellect, clarity, focus, and innovation.

Combined Accent (Green + Yellow):
- Lime / Chartreuse / Duo-tone Green-to-Yellow gradients (e.g., linear-gradient(135deg, #10B981, #EAB308))
- Used for special badges, interactive highlights, primary CTAs, active indicators, and subtle visual focal points.

Supporting:
- Muted slate, cool gray tones, and subtle border lines for hierarchy and depth.
```

### Color Usage Guidelines:

1. **Restraint and Balance:** Green and yellow should be used deliberately for accents, status badges, buttons, active links, and highlights without overwhelming readability or creating visual noise.
2. **Accessible Contrast:** Ensure all green and yellow text/elements meet WCAG 2.2 AA contrast standards against both dark and light backgrounds.
3. **Design Tokens:** Implement the palette using CSS variables (`--color-primary-green`, `--color-accent-yellow`, `--gradient-green-yellow`, etc.) so themes and accents can be managed centrally and globally.
4. **Theme Harmony:** Provide tailored green and yellow shades for both dark mode and light mode to ensure optimal optical balance and readability.

---

# 95. LOGO

The initial logo can be typography-based:

```text
NDOLI
```

Optional monogram:

```text
N
```

Do not create an overly complicated logo.

---

# 96. FAVICON

Create a clean favicon based on:

```text
N
```

or:

```text
ND
```

It must remain recognizable at small sizes.

---

# 97. HOMEPAGE SECTION ORDER

Recommended order:

```text
1. Navigation
2. Hero
3. Introduction
4. Featured Project — IHKIP
5. Selected Projects
6. What I Build
7. Experience
8. Research / Articles
9. Open Source
10. Technology
11. About preview
12. Contact CTA
13. Footer
```

The exact order can be optimized after testing.

---

# 98. WHAT I BUILD

Use capability-based categories rather than generic skill bars.

Example:

### Software Systems

Designing and building practical software platforms.

### Intelligent Systems

Exploring AI, RAG, local LLMs, and intelligent workflows.

### Digital Platforms

Building web-based systems for real-world organizational needs.

### Infrastructure

Deploying and maintaining reliable software environments.

### Research & Experimentation

Investigating new approaches and documenting lessons learned.

---

# 99. EXPERIENCE PREVIEW

Homepage should show a short timeline.

Example:

```text
Experience
────────────

IT / Software Development
Selected professional experience

System Development
Selected projects

Current
Software + AI + Technology
```

Only use factual dates and positions.

---

# 100. TECHNOLOGY SECTION

Do not display 50 logos.

Show technologies that matter.

Potential grouping:

```text
Languages
Python
JavaScript
HTML
CSS

Frameworks
Django

Data
PostgreSQL
pgvector

Infrastructure
Docker
Linux
Redis

AI
RAG
Local LLMs
Embeddings
AI orchestration

Tools
Git
GitHub
```

Only show verified/current technologies.

---

# 101. FOOTER

Footer should contain:

```text
NDOLI Jean Damascene

Technology professional building practical software,
intelligent systems, and digital platforms.

Projects
Research
Articles
GitHub
Contact

© <current year> NDOLI Jean Damascene
```

Do not clutter the footer.

---

# 102. CONTACT CTA

End major pages with a contextual CTA.

Example:

> Have a project, technical idea, research opportunity, or collaboration in mind?

Buttons:

```text
Get in touch
Explore projects
```

---

# 103. RELATED CONTENT

Project pages should link to:

* related projects;
* articles;
* research;
* GitHub repositories.

Articles should link to:

* related articles;
* relevant projects;
* research.

This creates a strong internal knowledge graph.

---

# 104. INTERNAL LINKING

Use meaningful anchor text.

Good:

> Read the IHKIP architecture case study.

Bad:

> Click here.

---

# 105. SEARCH ENGINE ENTITY STRATEGY

The website should consistently use:

```text
NDOLI Jean Damascene
NDOLI
ndoli.dev
```

Avoid unnecessary variations of the person's name.

Projects should consistently use their official project names.

---

# 106. OPEN GRAPH

Every major public page should have an appropriate social preview.

Default:

```text
NDOLI Jean Damascene
ndoli.dev
```

Project:

```text
IHKIP — Intelligent Health Knowledge & Information Platform
```

Article:

```text
Article title
NDOLI.DEV
```

---

# 107. SOCIAL PREVIEW IMAGE

Generate a consistent OG image system.

Possible layout:

```text
NDOLI
────────────
Page Title
Short descriptor
ndoli.dev
```

Project pages should have project-specific OG images.

---

# 108. PWA

PWA support is optional.

Do not implement it merely because it is fashionable.

If implemented:

* valid manifest;
* icons;
* installability;
* correct theme;
* offline strategy;
* no broken caching.

---

# 109. RSS

Implement RSS if article publishing becomes active.

Recommended:

```text
/feed/
```

or:

```text
/rss.xml
```

---

# 110. SITEMAP SEGMENTATION

If content becomes large, support separate sitemaps:

```text
/sitemap.xml
/sitemap-projects.xml
/sitemap-articles.xml
/sitemap-research.xml
```

Only necessary at scale.

---

# 111. INTERNATIONALIZATION

Initial language:

```text
English
```

Architecture should not make future localization impossible.

Potential future:

```text
Kinyarwanda
French
```

Do not build full multilingual infrastructure unless there is a real need.

---

# 112. CONTENT EDITOR

The admin should support Markdown or rich text.

If Markdown is used:

* sanitize rendered HTML;
* whitelist safe HTML;
* protect against XSS;
* support code blocks;
* support links.

---

# 113. CODE BLOCKS

Technical articles must support syntax highlighting.

Languages may include:

```text
Python
JavaScript
HTML
CSS
SQL
Bash
JSON
YAML
Dockerfile
```

---

# 114. DOCUMENTATION

Technical documentation should be treated as first-class content.

Potential documentation:

```text
Architecture
Deployment
API
Research notes
Technical decisions
Project guides
```

---

# 115. ARCHITECTURE DECISION RECORDS

For important technical choices, optionally maintain:

```text
docs/adr/
```

Example:

```text
ADR-001 Django as primary web framework
ADR-002 PostgreSQL as primary database
ADR-003 Server-side rendering strategy
ADR-004 VPS deployment strategy
```

This is especially useful for future maintenance.

---

# 116. FUTURE EXPANSION

The architecture should allow:

```text
Companies
Products
Startups
Speaking
Courses
Books
Publications
Podcasts
Media
Awards
Certifications
Community
Newsletter
```

Do not implement these until they have real content.

---

# 117. PERSONAL DASHBOARD

A private dashboard may be added in the future.

Possible:

```text
/content/
analytics/
drafts/
projects/
messages/
```

This must remain protected.

---

# 118. ADMIN AUTHENTICATION

Use strong authentication.

Future options:

* 2FA;
* passkeys;
* OTP;
* IP restrictions where practical;
* rate limiting.

Never weaken authentication for convenience.

---

# 119. PRIVACY

Do not publish:

* personal addresses;
* private phone numbers;
* private emails;
* sensitive documents;
* private client information;
* confidential project details.

---

# 120. LEGAL

Create:

```text
/privacy/
/terms/
```

when needed.

Content must accurately describe actual data collection.

Do not copy legal policies from another website.

---

# 121. COOKIE CONSENT

Only implement a cookie banner if the website actually uses cookies that require consent.

Do not add a cookie banner simply because other websites have one.

---

# 122. ACCESSIBILITY OF DARK MODE

Both themes must meet readability and contrast requirements.

Never rely solely on color.

---

# 123. MOBILE NAVIGATION

Mobile navigation must be:

* simple;
* keyboard accessible;
* screen-reader accessible;
* easy to close;
* non-blocking.

---

# 124. SCROLL BEHAVIOR

Use smooth scrolling only where appropriate.

Respect:

```text
prefers-reduced-motion
```

Do not hijack browser scrolling.

---

# 125. LOADING STATES

For dynamic content:

```text
Loading
Empty
Error
Success
```

must all be handled.

Do not leave blank UI when an API fails.

---

# 126. GITHUB API FAILURE

If GitHub integration fails:

> GitHub data temporarily unavailable.

The rest of the website must continue working.

---

# 127. CONTACT FAILURE

If email delivery fails:

* log the failure;
* show a user-friendly message;
* do not expose SMTP errors.

---

# 128. DATABASE FAILURE

Do not expose database exceptions.

Production should show a controlled error page.

---

# 129. OBSERVABILITY

Logs should include:

* application errors;
* failed requests where useful;
* security events;
* contact failures;
* background task failures.

Do not log sensitive credentials.

---

# 130. RATE LIMITING

Apply rate limits to:

```text
Contact form
Login
Search if abused
Admin endpoints
API endpoints
```

Do not unnecessarily rate-limit ordinary page views.

---

# 131. CACHING

Cache content where useful.

Possible:

```text
Homepage
Project lists
Article lists
GitHub API responses
```

Invalidate cache when content changes.

Do not cache private/admin responses.

---

# 132. DATABASE QUERY OPTIMIZATION

Use:

```text
select_related
prefetch_related
indexes
pagination
```

where appropriate.

Avoid N+1 queries.

---

# 133. PAGINATION

For large content lists:

```text
Articles
Projects
Research
```

use pagination.

Do not load hundreds of records onto one page.

---

# 134. CONTENT SEARCH ENGINE OPTIMIZATION

Articles should have:

* descriptive URLs;
* meaningful headings;
* useful introductions;
* original content;
* references where appropriate;
* internal links;
* optimized images.

---

# 135. NO SEO MANIPULATION

Never implement:

* hidden text;
* keyword stuffing;
* doorway pages;
* fake backlinks;
* cloaking;
* automatically generated spam;
* fake author profiles;
* fake reviews;
* duplicate pages created solely for rankings.

---

# 136. AUTHOR PROFILE

Articles and research should identify:

**NDOLI Jean Damascene**

The author profile should link to:

```text
/about/
```

---

# 137. ARTICLE DATES

Display:

```text
Published
Updated
```

when appropriate.

Do not modify dates solely to make old content appear new.

---

# 138. RESEARCH TRANSPARENCY

Research pages should support:

```text
Status
Method
Limitations
References
```

If a project is experimental, say so.

---

# 139. PROJECT TRANSPARENCY

Each project should indicate its status.

Example:

> **Status: In Development**

This is better than pretending every project is production-ready.

---

# 140. CASE STUDY EVIDENCE

Where possible, include:

* screenshots;
* architecture diagrams;
* code examples;
* GitHub repositories;
* measurable results;
* lessons learned.

Only use genuine evidence.

---

# 141. SCREENSHOT GALLERY

Project pages should support galleries.

Features:

* responsive images;
* lightbox;
* keyboard navigation;
* captions;
* alt text.

---

# 142. ARCHITECTURE DIAGRAMS

Important technical projects should support diagrams.

Example:

```text
User
 ↓
Web Application
 ↓
Application Services
 ↓
PostgreSQL
 ↓
External / Local AI
```

Diagrams must represent the actual architecture.

---

# 143. TECHNOLOGY RELATIONSHIPS

A project should be able to relate to technologies.

Example:

```text
IHKIP
├── Django
├── PostgreSQL
├── pgvector
├── Redis
├── Qwen
└── RAG
```

This allows filtering by technology later.

---

# 144. PROJECT FILTERING

Projects page should support filtering by:

```text
All
Software
AI
Healthcare
Research
Infrastructure
Open Source
Experimental
```

Keep filtering lightweight and accessible.

---

# 145. ARTICLES FILTERING

Support:

```text
All
AI
Software
Research
Technology
Career
```

---

# 146. SEARCH ENGINE FRIENDLY FILTERING

Do not generate thousands of indexable URLs for filters.

Filter pages should generally be client-side or appropriately controlled.

---

# 147. TECHNICAL SEO

Implement:

```text
clean URLs
canonical URLs
sitemap
robots
structured data
breadcrumbs
semantic HTML
fast pages
mobile responsiveness
image optimization
```

---

# 148. DOMAIN MIGRATION

If content previously existed on another domain:

```text
bazarwanda.me
```

and is moved to:

```text
ndoli.dev
```

preserve relevant URLs using 301 redirects where appropriate.

Do not blindly redirect unrelated URLs.

---

# 149. OLD DOMAIN

If `bazarwanda.me` remains active, it may eventually redirect to `ndoli.dev`.

Do not shut it down before migration is complete.

---

# 150. DNS

Production DNS should point:

```text
ndoli.dev → VPS
```

The application must not rely on the raw IP for public access.

---

# 151. SSL

Production must use:

```text
HTTPS
```

No HTTP-only production deployment.

Redirect:

```text
http://ndoli.dev
→
https://ndoli.dev
```

---

# 152. DOMAIN CANONICALIZATION

Preferred:

```text
https://ndoli.dev
```

Redirect:

```text
http://ndoli.dev
http://www.ndoli.dev
https://www.ndoli.dev
```

to:

```text
https://ndoli.dev
```

where DNS and deployment configuration permit.

---

# 153. ENVIRONMENT CONFIGURATION

Support:

```text
development
testing
production
```

Never use production credentials locally.

---

# 154. DEVELOPMENT ENVIRONMENT

Provide clear setup instructions.

Expected workflow:

```bash
git clone ...
cd ndoli-dev
cp .env.example .env
docker compose up
```

or equivalent.

---

# 155. LOCAL DEVELOPMENT

Developer should be able to run:

```text
Django
PostgreSQL
optional Redis
```

with minimal setup.

---

# 156. DATABASE MIGRATIONS

Every schema change must include migrations.

Never manually modify production tables without migration documentation.

---

# 157. MANAGEMENT COMMANDS

Useful commands may include:

```text
seed_demo_content
generate_sitemap
rebuild_search
import_github_data
```

Demo content must never be inserted into production automatically.

---

# 158. SEED DATA

If sample content is required:

* clearly mark it as demo;
* do not use fake professional achievements;
* do not deploy sample content accidentally.

---

# 159. CONTENT IMPORT

Future support may include importing:

```text
CV
GitHub projects
Markdown articles
research documents
```

Imports must require validation.

---

# 160. API

A public API is not required initially.

If needed in the future, design versioned endpoints:

```text
/api/v1/
```

Protect private endpoints.

---

# 161. HEADLESS ARCHITECTURE

Do not build a headless CMS architecture unless a real requirement appears.

The initial website should prioritize simplicity.

---

# 162. JAVASCRIPT

JavaScript should enhance the website, not control basic navigation.

Pages should remain usable with JavaScript unavailable where practical.

---

# 163. PROGRESSIVE ENHANCEMENT

Basic:

```text
HTML
CSS
server-rendered content
```

must work first.

JavaScript adds:

* filtering;
* animation;
* enhanced interactions;
* search suggestions;
* galleries.

---

# 164. FOOTER YEAR

Generate current year dynamically.

Do not hard-code:

```text
© 2026
```

forever.

---

# 165. TIMEZONE

Use a consistent timezone strategy.

Store dates in UTC where appropriate.

Render localized dates intentionally.

---

# 166. EMAIL LINKS

Use:

```text
mailto:
```

only for verified public professional email addresses.

---

# 167. EXTERNAL LINKS

External links should:

* use HTTPS;
* be verified;
* open appropriately;
* not expose private resources.

---

# 168. SECURITY HEADERS

Evaluate:

```text
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
Referrer-Policy
Permissions-Policy
```

Configure carefully to avoid breaking legitimate functionality.

---

# 169. CONTENT SECURITY POLICY

If implemented, test:

* fonts;
* images;
* analytics;
* GitHub integrations;
* scripts;
* admin.

Do not blindly use:

```text
unsafe-inline
```

everywhere.

---

# 170. DEPENDENCY MANAGEMENT

Keep dependencies minimal.

Regularly check:

```text
Django
Python
PostgreSQL drivers
frontend libraries
security packages
```

for security updates.

---

# 171. PYTHON

Use a currently supported Python version compatible with the chosen Django version.

Do not unnecessarily pin obsolete versions.

---

# 172. DJANGO

Use a currently supported Django release.

Prefer an LTS version when practical.

---

# 173. CODE QUALITY

Use:

```text
ruff
black
pytest
pytest-django
```

or equivalent tooling where appropriate.

---

# 174. TYPE SAFETY

Type hints should be used where they improve maintainability.

Do not add excessive typing complexity to simple Django code.

---

# 175. DOCUMENTATION COMMENTS

Comment why something exists, not what obvious code does.

Bad:

```python
# save project
project.save()
```

Good:

```python
# Keep GitHub metadata cached to avoid hitting the API on every page request.
```

---

# 176. ACCESSIBLE ICONS

Icons must have:

* accessible labels;
* hidden decorative semantics where appropriate.

Do not rely on icons alone to communicate actions.

---

# 177. BUTTONS VS LINKS

Use:

```text
button
```

for actions.

Use:

```text
a
```

for navigation.

---

# 178. FORMS

All forms must have:

* labels;
* validation;
* error messages;
* success state;
* keyboard support.

---

# 179. EMPTY STATES

If no projects exist:

> Projects are being prepared.

If no articles exist:

> Articles are coming soon.

Avoid broken empty pages.

---

# 180. LOADING EXPERIENCE

The website should render useful content quickly.

Avoid loading screens for ordinary pages.

---

# 181. HOMEPAGE SEO TITLE

Recommended:

> NDOLI Jean Damascene — Software Engineer & Technology Builder

Alternative:

> NDOLI — Software Engineer, AI & Technology Builder

Select the strongest accurate version.

---

# 182. HOMEPAGE META DESCRIPTION

Suggested:

> NDOLI Jean Damascene is an IT professional and software engineer building intelligent systems, digital platforms, and practical technology solutions.

Keep it accurate and concise.

---

# 183. ABOUT SEO

Suggested title:

> About NDOLI Jean Damascene | Software Engineer & Technology Builder

---

# 184. PROJECT SEO

Project titles should use:

```text
<Project Name> | NDOLI.DEV
```

Example:

> IHKIP — Intelligent Health Knowledge & Information Platform | NDOLI.DEV

---

# 185. ARTICLE SEO

Generate:

```text
<Article Title> | NDOLI.DEV
```

with unique descriptions.

---

# 186. AUTHOR ENTITY CONSISTENCY

Use exactly:

> NDOLI Jean Damascene

as the primary name throughout the website unless another verified professional format is intentionally used.

---

# 187. CONTACT INFORMATION

Only publish professional contact details intended for public use.

Never automatically expose:

* private phone;
* private address;
* personal documents.

---

# 188. CV SECURITY

The public résumé must not contain unnecessary sensitive information.

Avoid:

* national ID;
* passport number;
* private address;
* private phone unless intentionally public.

---

# 189. DOWNLOAD TRACKING

If resume downloads are tracked, track only the event.

Do not collect unnecessary identifying information.

---

# 190. CONTENT VERSIONING

For important research/project content, support:

```text
updated_at
version
```

where useful.

---

# 191. CHANGE LOG

Maintain a project changelog if the platform becomes significant.

Example:

```text
CHANGELOG.md
```

---

# 192. DESIGN QA

Before launch, inspect every major page at:

```text
375px
768px
1024px
1440px
1920px
```

Check:

* overflow;
* typography;
* spacing;
* images;
* navigation;
* forms.

---

# 193. BROWSER QA

Test:

```text
Chrome
Edge
Firefox
Safari where available
Mobile browsers
```

---

# 194. LAUNCH CHECKLIST

Before production:

```text
[ ] Domain connected
[ ] SSL working
[ ] HTTPS redirect working
[ ] Django production settings
[ ] DEBUG=False
[ ] Secrets secured
[ ] Database configured
[ ] Migrations applied
[ ] Static files working
[ ] Media working
[ ] Admin protected
[ ] Contact form tested
[ ] Sitemap working
[ ] Robots working
[ ] Canonicals correct
[ ] Open Graph correct
[ ] Structured data validated
[ ] 404 working
[ ] Security headers checked
[ ] Backups configured
[ ] Monitoring configured
[ ] Analytics configured if desired
[ ] Mobile QA complete
[ ] Accessibility QA complete
[ ] Performance QA complete
[ ] Google Search Console configured
```

---

# 195. GOOGLE SEARCH CONSOLE LAUNCH

After launch:

```text
1. Verify ndoli.dev
2. Submit sitemap.xml
3. Inspect homepage
4. Inspect important project pages
5. Request indexing where appropriate
6. Monitor indexing
7. Monitor search queries
8. Monitor Core Web Vitals
```

Do not repeatedly request indexing unnecessarily.

---

# 196. GOOGLE ANALYTICS STRATEGY

Search Console should be considered the primary source for:

```text
search queries
impressions
clicks
CTR
indexing
Core Web Vitals
```

Analytics should focus on:

```text
visitor behavior
project interest
article engagement
resume downloads
contact conversions
```

---

# 197. CONTENT STRATEGY

Long-term publishing should focus on:

```text
Build logs
Technical articles
Project case studies
Research notes
Architecture explanations
Lessons learned
Tutorials
Experiments
```

---

# 198. PERSONAL AUTHORITY STRATEGY

The website should gradually create an evidence trail:

```text
NDOLI
↓
Projects
↓
Technical documentation
↓
Articles
↓
Research
↓
GitHub
↓
External references
```

The objective is genuine professional visibility.

---

# 199. NOT A SOCIAL MEDIA REPLACEMENT

The website should not attempt to recreate LinkedIn.

It is the **owned professional identity**.

Social networks are optional distribution channels.

The website remains the source of truth.

---

# 200. CONTENT OWNERSHIP

All important professional content should live on `ndoli.dev` where practical.

External platforms should link back to the website.

---

# 201. PROJECT OWNERSHIP

For each project, record:

```text
Role
Ownership
Status
Repository
Live URL
```

Only display claims that are accurate.

---

# 202. PARTNERSHIPS

If a project involves an organization:

* use the organization's name accurately;
* do not imply endorsement;
* do not use logos without permission;
* document relationship type accurately.

---

# 203. TESTIMONIALS

Testimonials are optional.

If added:

* use real people;
* obtain permission;
* identify their role accurately;
* do not fabricate testimonials.

---

# 204. CLIENT LOGOS

Only display logos with permission or legitimate public usage rights.

---

# 205. METRICS

Metrics are useful only when genuine.

Good:

> Built with PostgreSQL and Django.

Potentially useful:

> X active users

only if the number can be verified.

Never create artificial metrics.

---

# 206. CALLS TO ACTION

CTAs should be purposeful.

Examples:

```text
Explore projects
Read research
View résumé
Read articles
Contact me
View GitHub
```

---

# 207. HOME PAGE DENSITY

Do not place every piece of information on the homepage.

Homepage should create curiosity and direct users deeper.

---

# 208. LONG-TERM CONTENT GRAPH

The architecture should eventually support:

```text
Person
│
├── Experience
│
├── Education
│
├── Skills
│
├── Projects
│   ├── IHKIP
│   └── Other projects
│
├── Research
│
├── Articles
│
├── Open Source
│
└── Publications
```

---

# 209. PROJECT → ARTICLE RELATIONSHIP

A project can have multiple articles.

Example:

```text
IHKIP
├── Architecture
├── RAG implementation
├── Local LLM deployment
└── Lessons learned
```

---

# 210. RESEARCH → PROJECT RELATIONSHIP

Research may lead to projects.

Example:

```text
Research
↓
Prototype
↓
Project
↓
Production
```

The website should make these relationships visible.

---

# 211. ARTICLE → PROJECT RELATIONSHIP

Articles should link to relevant project pages.

This strengthens discoverability and context.

---

# 212. RELATED CONTENT ENGINE

When appropriate:

```text
Project → Related Articles
Article → Related Projects
Research → Related Projects
```

Use manually curated relationships initially.

---

# 213. TAGGING

Tags should be controlled.

Potential:

```text
Django
Python
PostgreSQL
AI
RAG
Healthcare
Architecture
Security
DevOps
```

Avoid creating hundreds of tags.

---

# 214. TAXONOMY

Use:

```text
Category
Tags
Type
Status
```

appropriately.

Do not duplicate the same concept in five different taxonomies.

---

# 215. SEARCH RESULT UX

Search results should show:

```text
Title
Type
Excerpt
Date
```

Highlight matching terms where appropriate.

---

# 216. NO-RESULT SEARCH

Show:

> No results found.

Then suggest:

```text
Projects
Articles
Research
```

---

# 217. ERROR MONITORING PRIVACY

Before sending errors to third-party monitoring, ensure:

* emails are scrubbed where possible;
* form messages are not unnecessarily captured;
* credentials are never sent;
* tokens are removed.

---

# 218. BACKGROUND TASKS

Celery/Redis are not required for the initial site.

Introduce background workers only for tasks such as:

```text
GitHub synchronization
email processing
image processing
scheduled publishing
```

when actually necessary.

---

# 219. SIMPLE IS BETTER

The initial production website should remain simple.

Do not build:

```text
microservices
Kubernetes
complex message buses
multiple databases
AI agents
```

unless a genuine requirement appears.

---

# 220. AI FEATURES

AI features are optional.

The personal website itself does not need an AI chatbot.

If an AI feature is introduced later, it must have a clear purpose.

Examples:

```text
Project exploration assistant
Research assistant
Article search
Portfolio Q&A
```

Do not add AI simply for marketing.

---

# 221. AI CHATBOT POLICY

If eventually implemented:

* disclose that it is AI;
* don't make it impersonate NDOLI;
* don't allow it to invent professional claims;
* ground responses in published website content.

---

# 222. INTERNATIONAL SEARCH

The site should be understandable to international visitors.

Use clear professional English.

Avoid excessive local jargon.

Rwanda-related work can be clearly contextualized.

---

# 223. RWANDA CONTEXT

Where relevant, the website may communicate that NDOLI works within Rwanda's technology ecosystem.

Do not imply government affiliation unless formally established.

---

# 224. IHKIP POSITIONING

IHKIP should be presented as a significant project.

Potential positioning:

> An AI-assisted health knowledge intelligence platform exploring how authoritative clinical knowledge can be organized, retrieved, governed, and used through intelligent software systems.

This is more credible than claiming it is already a national platform unless that status is officially established.

---

# 225. RESEARCH CREDIBILITY

Research pages should clearly distinguish:

```text
Idea
Experiment
Prototype
Validated result
Production system
```

---

# 226. PROJECT MATURITY

Every project should have a maturity indicator.

Example:

```text
Concept
Prototype
Development
Active
Completed
Archived
```

---

# 227. PROFESSIONAL PHILOSOPHY

The About page may include a short philosophy.

Direction:

> Technology is valuable when it solves a real problem, remains maintainable, and creates measurable value for the people who use it.

Keep it concise.

---

# 228. CURRENT FOCUS

The site may have a "Current Focus" section.

Potential themes:

```text
Software Engineering
AI Systems
Knowledge Intelligence
Healthcare Technology
System Architecture
```

Only show areas that remain relevant.

---

# 229. NOW PAGE

Optional future page:

```text
/now/
```

Purpose:

What NDOLI is currently learning, building, or exploring.

This can make the website feel alive.

---

# 230. NEWS / UPDATES

Optional future section:

```text
/updates/
```

Use only for meaningful updates.

---

# 231. MEDIA KIT

Optional future page:

```text
/media/
```

Could include:

* short bio;
* long bio;
* professional portrait;
* project descriptions;
* logos;
* contact.

Useful for conferences and publications.

---

# 232. SPEAKING

Optional future page:

```text
/speaking/
```

Only implement when there are genuine speaking activities.

---

# 233. CERTIFICATIONS

Optional page:

```text
/certifications/
```

Each certification:

```text
name
issuer
date
credential_url
credential_id
expiry
```

Never invent certification IDs.

---

# 234. PUBLICATIONS

Optional page:

```text
/publications/
```

Support:

```text
title
authors
publisher
date
url
doi
abstract
```

Only use verified publications.

---

# 235. NEWSLETTER

Optional future feature.

If implemented:

* double opt-in;
* unsubscribe;
* privacy policy;
* secure storage;
* anti-spam;
* no unsolicited marketing.

---

# 236. ACCESSIBILITY STATEMENT

Optional:

```text
/accessibility/
```

if the site becomes sufficiently significant.

---

# 237. DESIGN PRINCIPLE

Every component should answer:

> Does this improve understanding, trust, navigation, or evidence of work?

If not, remove it.

---

# 238. ENGINEERING PRINCIPLE

Every dependency should answer:

> Why do we need this?

If the answer is weak, don't add it.

---

# 239. CONTENT PRINCIPLE

Every sentence should answer:

> Is this useful to the visitor?

If not, simplify or remove it.

---

# 240. BRAND PRINCIPLE

The website should feel:

```text
Confident
Technical
Human
Credible
Curious
Practical
Forward-looking
```

Not:

```text
Loud
Exaggerated
Generic
Corporate
Artificial
```

---

# 241. IMPLEMENTATION PHASES

The coding AI must implement in the following order.

## Phase 1 — Foundation

Implement:

```text
Django project
PostgreSQL
environment configuration
Docker
base templates
design tokens
navigation
footer
responsive layout
dark/light mode
error pages
```

---

## Phase 2 — Core Content

Implement:

```text
Home
About
Experience
Education
Skills
Projects
Project detail
Contact
Resume
```

---

## Phase 3 — Publishing

Implement:

```text
Articles
Research
Open Source
Tags
Categories
Search
Related content
```

---

## Phase 4 — SEO

Implement:

```text
metadata
canonical URLs
sitemap
robots
Open Graph
structured data
breadcrumbs
author metadata
```

---

## Phase 5 — Admin

Implement:

```text
Project admin
Article admin
Research admin
Experience admin
Education admin
Skills admin
Site settings
Media
SEO
```

---

## Phase 6 — Production Hardening

Implement:

```text
security headers
rate limiting
upload security
logging
monitoring
backup documentation
performance optimization
accessibility testing
```

---

## Phase 7 — Deployment

Deploy to:

```text
62.171.182.99
```

through the existing VPS/EasyPanel environment.

Configure:

```text
ndoli.dev
HTTPS
static files
media
PostgreSQL
production settings
```

---

## Phase 8 — Search Visibility

Configure:

```text
Google Search Console
sitemap submission
indexing validation
structured data validation
Open Graph testing
```

---

# 242. DEFINITION OF DONE

The website is not finished simply because it renders.

It is complete when:

```text
[ ] Homepage is polished
[ ] About is complete
[ ] Projects work
[ ] IHKIP case study works
[ ] Articles work
[ ] Research works
[ ] Open Source works
[ ] Experience works
[ ] Resume works
[ ] Contact works
[ ] Admin works
[ ] Mobile works
[ ] Dark mode works
[ ] Accessibility is tested
[ ] SEO is implemented
[ ] Sitemap works
[ ] Robots works
[ ] Structured data works
[ ] Canonicals work
[ ] SSL works
[ ] Security settings are production-ready
[ ] Backups documented
[ ] Monitoring configured
[ ] Performance optimized
[ ] No fake content
[ ] No broken links
[ ] No placeholder assets
[ ] No secrets committed
[ ] Production deployment verified
```

---

# 243. FINAL QUALITY STANDARD

Before declaring the project complete, ask:

### Identity

> Does this clearly communicate who NDOLI Jean Damascene is?

### Evidence

> Does the website demonstrate actual work rather than just listing skills?

### Technology

> Does the architecture remain maintainable?

### Design

> Does it look like a serious professional technology platform?

### Performance

> Is it fast?

### Accessibility

> Can different users navigate it?

### SEO

> Can search engines understand it?

### Security

> Is production properly hardened?

### Content

> Is every professional claim truthful?

### Future

> Can the site grow with NDOLI?

If any answer is no, continue improving.

---

# 244. LONG-TERM VISION

The final platform should evolve into:

```text
                         NDOLI.DEV
                             │
             ┌───────────────┼────────────────┐
             │               │                │
          PROFILE          WORK            KNOWLEDGE
             │               │                │
       ┌─────┼─────┐     ┌───┼────┐      ┌────┼────┐
       │     │     │     │   │    │      │    │    │
    About  Career  CV  Projects IHKIP Open Articles Research
       │                    │
       │                    │
    Education           Other Projects
       │
    Skills
```

`ndoli.dev` must become the **owned digital home of NDOLI Jean Damascene**.

It should remain useful regardless of whether the next major project is:

* AI;
* healthcare;
* enterprise software;
* cybersecurity;
* infrastructure;
* a startup;
* research;
* open source;
* or something completely different.

---

# 245. FINAL AI CODING INSTRUCTION

Before writing code:

1. Read this README completely.
2. Extract all requirements.
3. Create an implementation plan.
4. Identify dependencies.
5. Identify models.
6. Identify templates.
7. Identify services.
8. Identify security requirements.
9. Identify SEO requirements.
10. Identify testing requirements.
11. Implement Phase 1.
12. Test Phase 1.
13. Continue phase-by-phase.
14. Keep a development checklist.
15. Do not skip requirements silently.
16. If something cannot be implemented exactly, document the limitation and implement the closest secure, maintainable solution.
17. Do not replace the architecture with a generic portfolio template.
18. Do not invent personal information.
19. Do not use fake project data in production.
20. Optimize for long-term maintainability.

The final result must be a **production-quality personal technology platform**, not a simple portfolio landing page.

---

# 246. SUCCESS CRITERIA

NDOLI.DEV succeeds when a visitor can arrive from Google and quickly understand:

> **Who is NDOLI?**

> **What does he build?**

> **What is IHKIP?**

> **What other systems has he built?**

> **What does he research?**

> **What technical knowledge does he share?**

> **Where can I see his work?**

> **How can I contact him?**

And after exploring the site, the visitor should leave with one clear impression:

> **NDOLI is a technology builder who turns real-world problems into practical software systems.**

---

# END OF MASTER SPECIFICATION
