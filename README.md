# NDOLI.DEV — Personal Professional Website

## Production Specification & Implementation Guide

- **Domain:** `ndoli.dev`
- **Website:** [https://ndoli.dev](https://ndoli.dev/)
- **Owner:** NDOLI Jean Damascene
- **Role:** IT Professional · Software Developer · Systems Builder
- **Primary Goal:** Build a strong professional identity and searchable online presence independent of social-media platforms.

---

# 1. Project Vision

Build a premium, modern, fast, professional personal website for **NDOLI Jean Damascene**.

The website must not look like a generic developer portfolio. It should communicate:

* **Who I am**
* **What I build**
* **What technologies I work with**
* **My professional experience**
* **My education**
* **My projects**
* **My technical capabilities**
* **My work philosophy**
* **My interest in AI, healthcare technology, software engineering, and digital systems**
* **How organizations, companies, recruiters, and collaborators can work with me**

The website should establish `ndoli.dev` as my primary professional identity on the web.

The site should be optimized so that Google and other search engines can understand that:
> **NDOLI Jean Damascene** is an IT professional and software/system developer from Rwanda who builds practical digital systems, AI-assisted platforms, and enterprise software.

---

# 2. Core Objectives

### Primary Objectives
* Establish a strong personal brand.
* Become discoverable through Google Search.
* Showcase serious technical projects.
* Demonstrate professional experience.
* Build credibility with organizations and employers.
* Create a permanent professional identity independent of LinkedIn.
* Make it easy for people to contact me.
* Showcase software engineering and system architecture skills.
* Showcase selected AI/health technology work without making the website only about AI.
* Create a foundation that can grow for many years.

### Secondary Objectives
The website should eventually support:
* Technical articles
* Project case studies
* Open-source projects
* Speaking
* Consulting
* Collaboration
* Research
* Downloadable CV
* Professional references
* Certificates
* Achievements
* Developer resources

---

# 3. Brand Positioning

### Name
**NDOLI Jean Damascene**  
Short brand: **NDOLI**  
Domain: **ndoli.dev**

### Suggested Positioning
* **Primary:** IT Professional & Software Developer
* **Secondary:** Building practical digital systems, intelligent software, and technology solutions.
* **Alternative positioning:** Software Developer & Systems Builder

### Tone & Communication
The website must avoid exaggerated claims such as:
* *"World's best developer"*
* *"AI genius"*
* *"Expert in everything"*
* *"Revolutionary developer"*

The tone must be:
* **Professional**
* **Confident**
* **Technical**
* **Honest**
* **Modern**
* **Clear**
* **Human**

---

# 4. Target Audience

Design the website for several key audiences:

### 4.1 Recruiters
They should quickly find:
* Name, Role & Headline
* Skills & Core Stack
* Professional Experience
* Education
* Featured Projects
* CV / Résumé
* Direct Contact Information

### 4.2 Companies
They should understand:
* What I can build
* Technologies I use
* Systems I have worked on
* Business & organizational problems I solve

### 4.3 Government / Institutions
The site should communicate:
* Seriousness and reliability
* Technical capability
* Digital transformation experience
* Ability to build institutional systems
* Deep understanding of secure and scalable architecture

### 4.4 Developers
They should be able to discover:
* GitHub profile and repositories
* Project details & Case studies
* Technologies & Tools
* Technical writing & Insights
* System Architecture diagrams
* Open-source work

### 4.5 Potential Collaborators
They should easily understand:
* My interests and research focus
* Current projects
* Areas where collaboration is possible
* How to get in touch

---

# 5. Technology Stack

Use a production-oriented, maintainable architecture.

### Recommended Stack

#### Frontend
* **HTML5** & semantic markup
* **Vanilla CSS3** (or modern CSS / Tailwind CSS if appropriate)
* **Modern JavaScript** (Vanilla JS / minimal Alpine.js if needed)
* Minimal external JavaScript dependencies
* Responsive design
* Accessible semantic HTML (WCAG 2.2 AA)

#### Backend
If backend functionality / content management is required:
* **Django**
* **Django REST Framework** where APIs are necessary
* **PostgreSQL** (with pgvector for AI/knowledge retrieval)

> **Rule:** Do NOT introduce unnecessary Django/database complexity if a static implementation is sufficient. The developer should choose the simplest architecture that satisfies the requirements cleanly and robustly.

---

# 6. Design Philosophy

The site must feel like a combination of:
* **Professional portfolio**
* **Engineering profile**
* **Personal brand**
* **Technical laboratory**
* **Digital résumé**

### Avoid
* Generic Bootstrap templates
* Excessive gradients or garish colors
* Excessive or distracting animations
* Generic stock photos
* Fake statistics or vanity metrics
* Fake testimonials or client logos
* Excessive glassmorphism
* Overly rounded cartoonish cards
* Huge meaningless hero text
* AI-generated-sounding portfolio clichés

> **Core Standard:** The design should communicate **Technical competence + professionalism + personality**.

---

# 7. Visual Direction

Create a premium developer identity:

### Recommended Characteristics
* Clean, distinctive typography
* Strong visual hierarchy and generous whitespace
* Subtle borders and crisp card layouts
* High-quality SVG icons
* Minimal, purposeful micro-animations
* Flawless mobile experience
* Sleek, high-contrast dark mode
* Refined, editorial light mode
* Responsive navigation
* Elegant project showcase cards
* Technical visual elements (code snippets, terminal aesthetics, architectural diagrams)

---

# 8. Color System

Use a modern, professional, clean, and premium color system using a combination of green and yellow.

### 1. Color Palette

#### Primary Colors:
* **Green 600:** `#16A34A` (Primary brand color for light mode)
* **Green 500:** `#22C55E` (Primary brand color for dark mode)
* **Yellow 400:** `#FACC15` (Vibrant accent & dark mode highlight)
* **Yellow 500:** `#EAB308` (Warm golden accent for light mode)

#### Neutral Colors (Slate Scale):
* **Slate 900:** `#0F172A` (Dark mode base background & deep typography)
* **Slate 800:** `#1E293B` (Dark mode surface cards)
* **Slate 700:** `#334155` (Dark mode borders & elevated cards)
* **Slate 600:** `#475569` (Subtle secondary text)
* **Slate 500:** `#64748B` (Muted metadata text)
* **Slate 200:** `#E2E8F0` (Light mode borders & light dividers)
* **Slate 50:** `#F8FAFC` (Light mode primary background)

#### Semantic Colors:
* **Success:** `#16A34A`
* **Warning:** `#FACC15`
* **Error:** `#EF4444`
* **Info:** `#3B82F6`

### 2. Gradients
* **Green $\rightarrow$ Yellow:** `linear-gradient(135deg, #16A34A 0%, #FACC15 100%)`
* **Yellow $\rightarrow$ Green:** `linear-gradient(135deg, #FACC15 0%, #16A34A 100%)`
* **Green $\rightarrow$ Yellow $\rightarrow$ Green:** `linear-gradient(135deg, #16A34A 0%, #FACC15 50%, #22C55E 100%)`

### 3. Usage Guidelines
1. **Green is the primary brand color:** Use for primary buttons, links, icons, highlights, and success states.
2. **Yellow is the accent color:** Use for highlights, CTAs, important badges, and attention elements.
3. **Synergy:** Use green and yellow together to create energy, positivity, growth, and clarity.
4. **Accessibility:** Maintain strict **WCAG 2.2 AA** high contrast across light and dark modes.

---

# 9. Typography

Use modern, highly legible professional typography:

### Recommended Fonts
* **Primary UI Font:** Inter / Geist / Manrope / IBM Plex Sans
* **Monospace Code Font:** JetBrains Mono / Fira Code

### Rules
* Maximum 1 primary UI font + 1 monospace font.
* Clear heading scale ($H_1$ to $H_6$) with distinct weights and line-heights.

---

# 10. Website Structure

### Primary Routes
```text
/                  -> Home
/about             -> About Me & Professional Story
/experience        -> Experience Timeline & Roles
/projects          -> Project Portfolio
/projects/[slug]   -> Deep-dive Project Case Studies
/skills            -> Grouped Technical Capabilities
/writing           -> Technical Articles & Insights
/writing/[slug]    -> Full Article View
/contact           -> Contact Form & Verified Profiles
/cv                -> Digital / Printable CV & Resume
```

### Optional Future Routes
```text
/now               -> Current Activities & Learning
/uses              -> Tools, Hardware & Software Setup
/speaking          -> Talks & Workshops
/research          -> Research Papers & Prototypes
/open-source       -> Public Repositories & Packages
/certifications    -> Verified Credentials
```

---

# 11. Homepage

The homepage is the primary entry point and must communicate identity instantly.

### Hero Section
* **Identity:** NDOLI Jean Damascene
* **Headline:** IT Professional & Software Developer
* **Supporting Text:**  
  > *I build practical digital systems, intelligent software, and technology solutions that solve real-world problems.*
* **Primary CTA:** `View My Work`
* **Secondary CTA:** `Get In Touch`
* **Additional CTA:** `Download CV`

---

# 12. Homepage Sections

Recommended layout order:

```text
1. Hero
   ↓
2. Professional Snapshot
   ↓
3. Featured Projects
   ↓
4. Technical Skills
   ↓
5. Experience
   ↓
6. Selected Achievements
   ↓
7. Current Focus
   ↓
8. Writing / Insights
   ↓
9. Contact CTA
   ↓
10. Footer
```

---

# 13. Professional Snapshot

A clear summary statement:
> *I am an IT professional and software developer focused on building practical digital systems. My work spans web applications, backend systems, databases, AI-assisted software, networking, cybersecurity, and technology solutions for real-world organizations.*

---

# 14. Featured Projects

Showcase **3 to 6** major projects. Each card must include:
* Project Name
* Short Description
* Problem Context & Solution
* Technologies Used
* Current Status (e.g., Active Development, Prototype, Production)
* Role
* Live Demo Link (if available)
* GitHub Link (where public)
* Screenshots / UI Previews

> **Standard:** Do NOT fabricate project metrics or statistics (e.g., never claim *"Reduced processing time by 98%"* unless verified).

---

# 15. Project Case Studies

Every major project case study page (`/projects/[slug]`) should be structured logically:

```text
• Project Overview
• Problem Context
• My Role
• Architecture Diagram
• Technology Stack
• Implementation Details
• Key Challenges & Solutions
• Security & Performance Considerations
• Results & Impact
• Lessons Learned
• Future Improvements
• Links & Resources
```

---

# 16. IHKIP Project

**IHKIP** must be highlighted as a flagship engineering project.

* **Positioning:** Health Knowledge Intelligence Platform
* **Key Areas to Cover:**
  * Knowledge management challenges in healthcare
  * Authoritative search & semantic retrieval
  * AI-assisted consultation workflows
  * Knowledge governance & clinical safety guardrails
  * Secure architecture: Django, PostgreSQL, pgvector, Redis, Qwen/local LLM orchestration
* **Factual Integrity Rule:**
  * Do not claim unverified government adoption, official ministry endorsements, or clinical trials unless confirmed.
  * Clearly label status: *Personal Project / Prototype / Research Platform*.

---

# 17. Technical Skills

Organize skills into clear, meaningful categories:

### Programming
* Python
* JavaScript
* HTML5 / CSS3
* C++
* C#

### Backend & APIs
* Django & Django REST Framework
* RESTful API Design & Integration
* Authentication & Authorization (OAuth2, JWT, Session)
* Background Processing & Task Queues

### Databases
* PostgreSQL
* SQL & Schema Optimization
* pgvector (Vector Embeddings)

### AI & Intelligent Systems
* Retrieval-Augmented Generation (RAG)
* LLM Orchestration & Prompt Engineering
* Local LLM Inference
* Embeddings & Vector Similarity Search
* AI Assistants & Tool Calling

### Infrastructure & DevOps
* Linux / Unix Administration
* Docker & Containerization
* VPS Management & Deployment
* Redis Caching
* Git & Version Control

### Systems & Security
* Computer Networking & Routing
* Cybersecurity Fundamentals & Hardening
* System Administration & Technical Support
* WordPress Maintenance & Customization

> **Rule:** Only list technologies that can be genuinely demonstrated, explained, and defended.

---

# 18. Experience

Present a clean, chronological timeline with verified employment history:

* **GIRA LTD** — *IT Manager*  
  `June 2023 – Present`  
  Responsibilities and achievements documented based on verified organizational scope.
* **ES SUMBA IT** — *IT / Technical Role*  
  `August 2021 – May 2024`
* **NIRDA** — *Intern / Team Leader*

> **Rule:** Document factual responsibilities only; never invent titles or achievements.

---

# 19. Education

* **Degree:** Bachelor of Science in Information Technology
* **Institution:** University of Rwanda
* **Graduation:** 2026

---

# 20. Certifications

Dedicated section for verified certifications across:
* Networking
* Cybersecurity
* IT & Cloud
* Software Development
* AI & Machine Learning

Each entry includes: `Certification Name`, `Issuing Organization`, `Date`, `Credential ID`, and `Verification Link`.

---

# 21. GitHub Integration

* Showcase curated, selected repositories instead of dumping all repos.
* Show: Repository name, description, main language, tech tags, stars/forks (cached), and repository link.
* Never expose private or client repositories.

---

# 22. Open Source

A dedicated section for:
* Public repositories and developer tooling
* Reusable packages, libraries, and boilerplates
* Technical documentation and guides

---

# 23. Writing / Technical Blog

URL: `/writing`

### Purpose
* Increase Google discoverability for technical queries
* Demonstrate technical problem-solving and architectural thinking
* Share knowledge with the engineering community

### Article Categories
* Software Engineering
* Django & Python
* AI & Local RAG Architectures
* Healthcare Technology
* Cybersecurity & Infrastructure
* DevOps & VPS Deployment
* Rwanda Technology Ecosystem
* Engineering Lessons Learned

### Article Metadata
Title, Slug, Summary, Published Date, Updated Date, Category, Tags, Author, Reading Time, Content (Markdown), Related Projects.

---

# 24. SEO Strategy

SEO is a primary goal.

### Primary Keywords
Natural variations of:
```text
NDOLI Jean Damascene
NDOLI
NDOLI IT
NDOLI developer
NDOLI software developer
NDOLI Rwanda
Jean Damascene NDOLI
ndoli.dev
```

> **Strict Rule:** Avoid keyword stuffing. Write natural, helpful, high-value technical content.

---

# 25. Homepage SEO

* **Title:** `NDOLI Jean Damascene | IT Professional & Software Developer`
* **Meta Description:** `NDOLI Jean Damascene is an IT professional and software developer from Rwanda building practical digital systems, intelligent software, and technology solutions.`
* **Canonical URL:** `https://ndoli.dev/`

---

# 26. Open Graph

Implement complete OG tags across all pages:
```html
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://ndoli.dev/static/images/og-preview.jpg">
<meta property="og:url" content="...">
<meta property="og:type" content="website">
```
* Custom social preview image: `1200 × 630` px with clean typography and branding.

---

# 27. Twitter / X Metadata

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="...">
<meta name="twitter:description" content="...">
<meta name="twitter:image" content="...">
```

---

# 28. Structured Data (JSON-LD)

Include valid Schema.org markup:

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "NDOLI Jean Damascene",
  "url": "https://ndoli.dev",
  "jobTitle": "IT Professional & Software Developer",
  "alumniOf": {
    "@type": "CollegeOrUniversity",
    "name": "University of Rwanda"
  },
  "sameAs": [
    "https://github.com/...",
    "https://linkedin.com/in/..."
  ],
  "knowsAbout": [
    "Software Engineering",
    "Python",
    "Django",
    "PostgreSQL",
    "Artificial Intelligence",
    "Retrieval-Augmented Generation",
    "Healthcare Information Systems"
  ]
}
```

---

# 29. Website Schema

Implement corresponding schemas: `WebSite`, `WebPage`, `Person`, `Article`, and `BreadcrumbList`.

---

# 30. Sitemap

* Generate `/sitemap.xml` automatically.
* Include all canonical, indexable public URLs (`/`, `/about`, `/projects`, `/writing`, etc.).
* Exclude `/admin/`, private pages, API routes, or test pages.

---

# 31. Robots.txt

```text
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/private/

Sitemap: https://ndoli.dev/sitemap.xml
```

---

# 32. Search Engine Indexing

* Register domain in **Google Search Console** and **Bing Webmaster Tools**.
* Submit `sitemap.xml`.
* Validate canonical tags, mobile usability, and schema rendering.

---

# 33. Personal Knowledge Graph Strategy

Create a consistent entity graph across web platforms:
```text
ndoli.dev  <-->  GitHub  <-->  LinkedIn  <-->  Verified Profiles
```
Use `sameAs` only for verified personal profiles.

---

# 34. Google Discoverability

Achieve organic search ranking through:
1. Publishing original, deeply technical articles.
2. Creating comprehensive case studies with architecture diagrams.
3. Fast load times and Core Web Vitals compliance.
4. Clean internal linking.
5. Consistent entity references.

---

# 35. Content Strategy

Focus on technical topics grounded in real experience:
* *Building Production Django Applications*
* *Building a Local RAG System with Django and PostgreSQL*
* *Designing Knowledge Retrieval Systems for Clinical Information*
* *Deploying Django Applications on a VPS with Docker*
* *Building Digital Systems for Real-World Problems in Rwanda*

---

# 36. "Now" Page

URL: `/now`
A live page showing what NDOLI is currently:
* **Building** (Active projects)
* **Learning** (New technologies, frameworks, or concepts)
* **Researching** (AI, systems, healthcare IT)
* **Reading** (Books, papers, technical specifications)

---

# 37. Contact Page

URL: `/contact`

* Direct professional email
* GitHub and verified professional profiles
* Clean contact form with fields: `Name`, `Email`, `Subject`, `Message`
* Security: CSRF protection, server-side validation, rate limiting, and spam honeypot.

---

# 38. CV / Résumé

* URL: `/cv` (Indexable HTML résumé format)
* Clean button: `Download PDF`
* Contains: Summary, Technical Skills, Experience, Education, Projects, Certifications, Contact.

---

# 39. Accessibility

* **Standard:** Target **WCAG 2.2 AA**.
* Accessible keyboard navigation with visible `:focus-visible` rings.
* Meaningful `alt` text for images.
* Accessible form inputs with `<label>` bindings.
* Semantic HTML5 elements (`<header>`, `<main>`, `<nav>`, `<article>`, `<section>`, `<footer>`).
* Respect `@media (prefers-reduced-motion: reduce)`.

---

# 40. Performance

Lighthouse targets:
* **Performance:** 90+
* **Accessibility:** 95+
* **Best Practices:** 95+
* **SEO:** 95+

Optimizations:
* Responsive images with modern formats (AVIF / WebP)
* Preloaded critical fonts
* Minified CSS & deferred non-critical JS
* Browser caching headers

---

# 41. Security

* Strict **HTTPS** enforcement
* Security headers: `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, and a tight `Content-Security-Policy`
* CSRF & XSS protection
* Rate limiting on form submission
* Never commit secrets (`.env` files, API keys, passwords, private keys) to Git.

---

# 42. Privacy

* Privacy-first approach: no intrusive ad trackers or cross-site tracking scripts.
* Privacy-friendly analytics (e.g., cookieless / self-hosted if used).

---

# 43. Analytics

Track meaningful events without collecting invasive personal data:
* Page views
* Project views & Case study reading depth
* CV PDF downloads
* Contact form conversions
* External GitHub clicks

---

# 44. Navigation

* **Desktop Navigation:** `Home`, `About`, `Experience`, `Projects`, `Skills`, `Writing`, `Contact`
* **Utility Items (Right):** GitHub Link, CV Button, Dark/Light Theme Toggle
* **Mobile:** Clean, accessible slide-out or dropdown menu with full keyboard trap support.

---

# 45. Footer

* Name & Title: **NDOLI Jean Damascene** — *IT Professional & Software Developer*
* Copyright notice: `© 2026 NDOLI Jean Damascene`
* Quick links to primary pages and social links (GitHub, Email, LinkedIn)
* Lightweight and un-cluttered.

---

# 46. Micro-interactions

Subtle, high-performance CSS interactions:
* Button hover & press states
* Card elevation & border glow on hover
* Smooth theme transition
* Copy-to-clipboard for code blocks
* Smooth page transitions

---

# 47. Mobile Design

Mobile-first design tested across breakpoints:
`320px`, `375px`, `390px`, `430px`, `768px`, `1024px`, `1280px`, `1440px+`

* Zero horizontal overflow
* Minimum touch target size: `44 × 44` px
* Responsive typography and fluid grid layouts

---

# 48. Content Management

Structured content schemas:

```text
Project:
  title, slug, summary, description, featured, status, role,
  technologies, repository_url, live_url, image, created_at, updated_at

Article:
  title, slug, excerpt, content, category, tags,
  featured_image, published, published_at, updated_at
```

---

# 49. Admin

If Django is used:
* Secure Django Admin interface for Projects, Articles, Skills, Experience, Certifications.
* Protected under non-default URL path.
* Strong password & session security.

---

# 50. API (Optional)

If needed for dynamic integrations:
* `/api/projects/`
* `/api/articles/`
* Built with pagination, rate limiting, and proper serialization.

---

# 51. Database

When dynamic backend is used: **PostgreSQL**

```text
Models:
• Profile
• Experience
• Education
• SkillCategory
• Skill
• Project
• ProjectTechnology
• Article
• ArticleTag
• Certification
• SocialLink
• ContactMessage
```

---

# 52. Deployment

* **Host VPS IP:** `62.171.182.99` *(do not hardcode in application code; use environment variables)*
* **Domains:** `ndoli.dev` and `www.ndoli.dev`
* **Architecture:**
  ```text
  Internet  -->  DNS  -->  Reverse Proxy (Nginx / Caddy / EasyPanel)  -->  Web App (Django / Static)  -->  PostgreSQL
  ```

---

# 53. Domain Canonicalization

* **Canonical Domain:** `https://ndoli.dev`
* **Redirects:**
  * `http://ndoli.dev` $\rightarrow$ `https://ndoli.dev` (301)
  * `http://www.ndoli.dev` $\rightarrow$ `https://ndoli.dev` (301)
  * `https://www.ndoli.dev` $\rightarrow$ `https://ndoli.dev` (301)

---

# 54. Environment Variables

Provide `.env.example`:

```bash
DEBUG=False
SECRET_KEY=your-secure-secret-key-here
ALLOWED_HOSTS=ndoli.dev,www.ndoli.dev,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/ndoli_dev
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_HOST_USER=contact@ndoli.dev
EMAIL_HOST_PASSWORD=your-smtp-password
DEFAULT_FROM_EMAIL=contact@ndoli.dev
GITHUB_TOKEN=
ANALYTICS_ID=
```

---

# 55. Git Repository Structure

```text
ndoli.dev/
├── README.md
├── LICENSE
├── .gitignore
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── docs/
│   ├── architecture.md
│   ├── deployment.md
│   ├── seo.md
│   └── content.md
├── src/
│   ├── core/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
├── tests/
└── scripts/
```

---

# 56. Git Workflow

* Branching strategy: `main` $\leftarrow$ `develop` $\leftarrow$ `feature/*` / `fix/*`
* Semantic commit messages:
  * `feat: add project case study pages`
  * `feat: implement structured data JSON-LD`
  * `fix: improve mobile navigation keyboard focus`
  * `perf: optimize images to WebP format`
  * `sec: harden CSP headers and contact rate limiting`

---

# 57. Testing Suite

* **Functional:** Navigation, Project detail views, Article rendering, Contact form submission, CV download.
* **Security:** CSRF protection, input validation, secure cookies, SQL injection prevention.
* **SEO:** Meta tags, canonical links, valid Open Graph, sitemap generation, JSON-LD schema validity.
* **Accessibility:** Automated axe-core checks, keyboard navigation audit, contrast ratios.

---

# 58. Error Pages

Polished, branded custom error pages:
* `404 Not Found` ("*This page could not be found.*" + Back Home & View Projects buttons)
* `403 Forbidden`
* `500 Server Error` (Never leak stack traces or internal environment details)

---

# 59. Empty States

If a category or list has no entries yet, display elegant empty state components with clear guidance instead of broken layouts.

---

# 60. Loading States

* Clean skeleton loaders for dynamic content
* Graceful fallbacks and timeout handling
* Zero jarring layout shifts (CLS < 0.1)

---

# 61. Project Statuses

Standardized labels:
* `Concept`
* `Prototype`
* `Active Development`
* `Production`
* `Archived`

---

# 62. Trust & Credibility

* Never fabricate client names, revenue numbers, user counts, awards, certifications, or partnerships.
* If any information is not yet verified by NDOLI Jean Damascene, omit it.

---

# 63. Personal Branding Consistency

Always use the exact full professional name:
> **NDOLI Jean Damascene** (Short: **NDOLI**)

Avoid inconsistent variations across pages and metadata.

---

# 64. Homepage SEO Content Mapping

The homepage must clearly answer:
* **Who?** NDOLI Jean Damascene
* **What?** IT Professional & Software Developer
* **Where?** Rwanda
* **What does he build?** Practical digital systems, intelligent software, AI-assisted tools, and enterprise applications.
* **What technologies?** Python, Django, PostgreSQL, JavaScript, AI/RAG, Linux, Docker, etc.
* **Where can visitors learn more?** Projects, Experience, Skills, Writing, GitHub, and CV.

---

# 65. Search-Friendly URLs

* Use semantic, descriptive slugs:  
  `/projects/ihkip`  
  `/projects/property-management-system`  
  `/writing/building-local-rag-with-django`
* Avoid opaque IDs (`/projects/123`, `?id=1`).

---

# 66. Search-Friendly Writing

Publish comprehensive, well-researched technical articles with code examples, architecture diagrams, and actionable takeaways.

---

# 67. Internal Linking Strategy

Interconnect all content clusters:
```text
Project (IHKIP)  -->  Tech Stack (Django, pgvector)  -->  Related Article (Local RAG)
Article  -->  Featured Projects  -->  About / Contact
```

---

# 68. Professional Call to Action

Natural, confident invitation to connect:
> *"Have a system to build, a technical problem to solve, or an opportunity in mind? Let's talk."*

---

# 69. "Current Focus" Section

Homepage widget highlighting active exploration:
* **AI-Assisted Software:** Exploring local LLM orchestration and vector search
* **Healthcare Technology:** Clinical knowledge retrieval and data governance
* **Backend Systems:** High-performance Django and PostgreSQL architectures
* **Digital Platforms:** Scalable web systems for real-world operations

---

# 70. "Technologies I Use" Section

Grouped logically by discipline:
* **Build:** Python · Django · JavaScript · HTML5 · CSS3
* **Data:** PostgreSQL · SQL · pgvector
* **AI:** RAG · LLM Orchestration · Embeddings · Vector Search
* **Infrastructure:** Linux · Docker · VPS · Git · Redis
* **Security:** Authentication · Secure APIs · System Hardening

---

# 71. Personal Photo

* Use a high-quality, professional headshot with neutral background when provided.
* Do not use AI-generated fake identity portraits.

---

# 72. Social Profiles

Centralized, verified links:
* **GitHub:** Public open-source code & activity
* **LinkedIn:** Professional network
* **Email:** Direct inquiries
* **X / Twitter:** Tech updates

---

# 73. No LinkedIn Dependency

* The website is completely self-contained and independent of third-party platforms.
* No required external embeds or logins.

---

# 74. Long-Term Strategy

`ndoli.dev` is the permanent, owned digital home of NDOLI Jean Damascene that compounds in search visibility and authority over time.

---

# 75. Future Features

Extensible architecture prepared for:
* Interactive architecture demos
* Searchable technical notes
* Public project changelog
* Developer tooling & cheat-sheets
* Newsletter subscription (double opt-in)

---

# 76. AI Coding Agent Instructions

1. Treat this document as the master authoritative specification.
2. Inspect the repository before modifying files.
3. Reuse clean patterns and avoid bloat.
4. Maintain strict factual honesty for all profile claims.

---

# 77. Implementation Order

* **Phase 1 — Foundation:** App architecture, styles, typography, green/yellow design tokens, base layouts, responsive navigation, dark/light theme toggle.
* **Phase 2 — Core Content:** Homepage, About, Experience, Skills, Projects showcase, Project Case Studies, CV, Contact.
* **Phase 3 — SEO:** Metadata, Canonicals, Open Graph, Twitter cards, JSON-LD schema, Sitemap, Robots.txt, Breadcrumbs.
* **Phase 4 — Content Platform:** Writing / Blog system, Categories, Tags, Markdown parser, Related projects engine.
* **Phase 5 — Performance:** Image optimization (WebP/AVIF), CSS/JS minification, caching headers, Lighthouse 90+ audit.
* **Phase 6 — Security:** CSP headers, CSRF tokens, form rate limiting, validation, secrets isolation.
* **Phase 7 — Deployment:** VPS configuration, reverse proxy setup, SSL certificate, 301 canonical redirects.
* **Phase 8 — Quality Assurance:** Cross-browser testing, mobile verification, accessibility audit, test suite execution.

---

# 78. Definition of Done Checklist

- [ ] **Design:** Premium appearance, responsive layout, dark/light modes working, WCAG 2.2 AA compliant.
- [ ] **Content:** Real information for Homepage, About, Experience, Skills, Projects, IHKIP Case Study, CV, Contact.
- [ ] **SEO:** Correct title & meta tags, canonical URL, sitemap.xml, robots.txt, JSON-LD Person/WebSite schema, OG cards.
- [ ] **Performance:** Fast initial load, optimized images, minimal JS, zero layout shifts.
- [ ] **Security:** HTTPS enforced, CSP & security headers active, CSRF protection, no secrets committed.
- [ ] **Deployment:** `ndoli.dev` live with SSL, `www` redirecting to apex domain, production settings enabled.

---

# 79. Important Development Rule

Do not optimize this website only for appearance. The final product must balance:
> **Brand + Credibility + SEO + Performance + Accessibility + Security + Maintainability**

---

# 80. Final Product Principle

The goal is to build a permanent, owned digital professional identity for **NDOLI Jean Damascene**. When someone searches for **NDOLI**, **NDOLI Jean Damascene**, or **NDOLI developer**, `ndoli.dev` must stand out as the authoritative, credible destination.

---

# 81. AI Agent Final Instruction

Execute the project systematically, adhering to every specification item in this document. Build a resilient, production-quality platform that serves NDOLI Jean Damascene for years to come.
