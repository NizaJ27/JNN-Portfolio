# Python Flask Portfolio - System Architecture

## Overview

A professional, multi-page portfolio website built with Python Flask, showcasing business and technical skills. Fully deployable to platforms like Render, Railway, or PythonAnywhere.

## Technology Stack

### Core Framework
- **Flask 3.0+**: Lightweight Python web framework
- **Jinja2**: Template engine (included with Flask)
- **Python 3.11+**: Programming language

### Frontend
- **HTML5/CSS3**: Structure and styling
- **Tailwind CSS**: Utility-first CSS framework (via CDN or build process)
- **Alpine.js**: Lightweight JavaScript framework for interactivity
- **HTMX** (optional): Modern interactions without heavy JavaScript

### Data Management
- **JSON**: Project data storage
- **YAML/JSON**: Configuration files
- **SQLite** (optional): For contact form submissions/analytics

### Testing
- **pytest**: Testing framework
- **pytest-cov**: Code coverage
- **pytest-flask**: Flask-specific testing utilities
- **pylint**: Code quality and linting
- **black**: Code formatting

### Development Tools
- **python-dotenv**: Environment variable management
- **Flask-Assets**: Asset management and bundling
- **Werkzeug**: WSGI utilities (included with Flask)

### Deployment
- **Gunicorn**: Production WSGI server
- **Render/Railway**: Cloud deployment platforms
- **Docker** (optional): Containerization
- **GitHub Actions**: CI/CD pipeline

## Project Structure

```
portfolio/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py              # Landing page route
│   │   ├── business.py          # Business section routes
│   │   ├── development.py       # Developer section routes
│   │   ├── projects.py          # Project portfolio routes
│   │   └── contact.py           # Contact form routes
│   ├── templates/
│   │   ├── base.html            # Base template with header/footer
│   │   ├── components/          # Reusable template components
│   │   │   ├── navigation.html
│   │   │   ├── footer.html
│   │   │   ├── card.html
│   │   │   └── button.html
│   │   ├── pages/
│   │   │   ├── index.html       # Landing page
│   │   │   ├── business.html    # Business section
│   │   │   ├── development.html # Developer section
│   │   │   ├── projects.html    # Projects listing
│   │   │   ├── project_detail.html
│   │   │   └── contact.html     # Contact page
│   │   └── errors/
│   │       ├── 404.html
│   │       └── 500.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── main.css         # Custom styles
│   │   │   └── tailwind.css     # Tailwind (if using build)
│   │   ├── js/
│   │   │   ├── main.js          # Custom JavaScript
│   │   │   └── alpine.js        # Alpine.js components
│   │   ├── images/
│   │   │   ├── profile/
│   │   │   ├── projects/
│   │   │   └── logos/
│   │   └── files/
│   │       └── Joshua-Nizamudin-Resume.pdf
│   ├── models/
│   │   ├── __init__.py
│   │   ├── project.py           # Project data model
│   │   └── resume.py            # Resume data model
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── data_loader.py       # Load JSON data
│   │   ├── filters.py           # Custom Jinja2 filters
│   │   └── helpers.py           # Helper functions
│   └── config.py                # Configuration classes
│
├── content/
│   ├── projects.json            # All project data
│   ├── resume.json              # Resume structured data
│   ├── about.json               # About me content
│   └── case_studies/            # Markdown case studies
│       ├── therapy-app.md
│       └── module14.md
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Pytest fixtures
│   ├── test_routes.py           # Route tests
│   ├── test_models.py           # Model tests
│   ├── test_utils.py            # Utility tests
│   └── test_integration.py      # Integration tests
│
├── migrations/                   # Database migrations (if using SQLite)
├── instance/                     # Instance-specific files (gitignored)
├── .venv/                        # Virtual environment (gitignored)
│
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Development dependencies
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── pytest.ini                    # Pytest configuration
├── .pylintrc                     # Pylint configuration
├── Procfile                      # For Render/Heroku deployment
├── render.yaml                   # Render deployment config
├── Dockerfile                    # Docker configuration (optional)
├── README.md                     # Project documentation
└── run.py                        # Application entry point
```

## Data Models

### Project Model (Python dataclass)

```python
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from datetime import date

@dataclass
class Project:
    """Represents a portfolio project"""
    id: str
    title: str
    slug: str
    tagline: str
    description: str
    category: str  # 'business', 'technical', 'academic', 'personal'
    tags: List[str]
    technologies: List[str]
    date: str
    duration: Optional[str] = None
    role: str = ""
    thumbnail: str = ""
    images: List[str] = field(default_factory=list)
    featured: bool = False
    links: Dict[str, str] = field(default_factory=dict)
    metrics: List[Dict[str, str]] = field(default_factory=list)
    has_case_study: bool = False
    
    @property
    def formatted_date(self) -> str:
        """Return formatted date string"""
        return self.date
    
    @property
    def is_recent(self) -> bool:
        """Check if project is from last 6 months"""
        # Implementation here
        return True
```

### Resume Model

```python
@dataclass
class Experience:
    title: str
    company: str
    location: str
    start_date: str
    end_date: str  # or 'Present'
    description: List[str]
    achievements: List[str]

@dataclass
class Education:
    degree: str
    major: str
    institution: str
    location: str
    graduation_date: str
    gpa: Optional[str] = None
    honors: List[str] = field(default_factory=list)

@dataclass
class Resume:
    personal_info: Dict[str, str]
    summary: str
    experience: List[Experience]
    education: List[Education]
    skills: Dict[str, List[str]]
    certifications: List[Dict[str, str]] = field(default_factory=list)
```

## Flask Application Structure

### App Factory Pattern (`app/__init__.py`)

```python
from flask import Flask
from app.config import Config

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Register blueprints
    from app.routes import main, business, development, projects, contact
    app.register_blueprint(main.bp)
    app.register_blueprint(business.bp)
    app.register_blueprint(development.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(contact.bp)
    
    # Register custom Jinja2 filters
    from app.utils.filters import register_filters
    register_filters(app)
    
    # Error handlers
    from app.routes import errors
    app.register_blueprint(errors.bp)
    
    return app
```

### Route Structure (Blueprint-based)

**Main Routes (`app/routes/main.py`):**
```python
from flask import Blueprint, render_template
from app.utils.data_loader import load_projects, load_resume

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Landing page"""
    recent_projects = load_projects(featured=True, limit=3)
    return render_template('pages/index.html', 
                         projects=recent_projects,
                         title='Joshua Nizamudin | Portfolio')
```

**Business Routes (`app/routes/business.py`):**
```python
from flask import Blueprint, render_template
from app.utils.data_loader import load_resume, load_projects

bp = Blueprint('business', __name__, url_prefix='/business')

@bp.route('/')
def index():
    """Business section main page"""
    resume = load_resume()
    business_projects = load_projects(category='business')
    return render_template('pages/business.html',
                         resume=resume,
                         projects=business_projects,
                         title='Business Professional')
```

**Projects Routes (`app/routes/projects.py`):**
```python
from flask import Blueprint, render_template, request, abort
from app.utils.data_loader import load_projects, load_project_by_slug

bp = Blueprint('projects', __name__, url_prefix='/projects')

@bp.route('/')
def index():
    """All projects with filtering"""
    category = request.args.get('category', 'all')
    projects = load_projects(category=category if category != 'all' else None)
    return render_template('pages/projects.html',
                         projects=projects,
                         selected_category=category,
                         title='All Projects')

@bp.route('/<slug>')
def detail(slug):
    """Individual project detail page"""
    project = load_project_by_slug(slug)
    if not project:
        abort(404)
    return render_template('pages/project_detail.html',
                         project=project,
                         title=project.title)
```

## Template Architecture (Jinja2)

### Base Template (`templates/base.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{{ description|default('Portfolio of Joshua Nizamudin') }}">
    <title>{{ title|default('Joshua Nizamudin') }}</title>
    
    <!-- Tailwind CSS CDN (or compiled version) -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Alpine.js for interactivity -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    
    {% block extra_head %}{% endblock %}
</head>
<body class="min-h-screen flex flex-col">
    {% include 'components/navigation.html' %}
    
    <main class="flex-grow">
        {% block content %}{% endblock %}
    </main>
    
    {% include 'components/footer.html' %}
    
    <!-- Custom JavaScript -->
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

### Component Templates

Components are included using Jinja2's `include` or macros:

```html
{# templates/components/card.html #}
{% macro project_card(project) %}
<div class="bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow p-6">
    <img src="{{ url_for('static', filename='images/projects/' + project.thumbnail) }}" 
         alt="{{ project.title }}"
         class="w-full h-48 object-cover rounded-md mb-4">
    <h3 class="text-xl font-bold mb-2">{{ project.title }}</h3>
    <p class="text-gray-600 mb-4">{{ project.tagline }}</p>
    <div class="flex flex-wrap gap-2 mb-4">
        {% for tech in project.technologies[:3] %}
        <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">
            {{ tech }}
        </span>
        {% endfor %}
    </div>
    <a href="{{ url_for('projects.detail', slug=project.slug) }}" 
       class="text-blue-600 hover:text-blue-800 font-semibold">
        View Project →
    </a>
</div>
{% endmacro %}
```

## Testing Strategy

### Test Configuration (`pytest.ini`)

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --verbose
    --cov=app
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80
```

### Test Fixtures (`tests/conftest.py`)

```python
import pytest
from app import create_app
from app.config import TestConfig

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app(TestConfig)
    return app

@pytest.fixture
def client(app):
    """Test client"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Test CLI runner"""
    return app.test_cli_runner()
```

### Example Tests (`tests/test_routes.py`)

```python
def test_index_page(client):
    """Test landing page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Joshua Nizamudin' in response.data

def test_business_page(client):
    """Test business section loads"""
    response = client.get('/business/')
    assert response.status_code == 200
    assert b'Business Professional' in response.data

def test_projects_filtering(client):
    """Test project filtering works"""
    response = client.get('/projects/?category=technical')
    assert response.status_code == 200
    # Add more assertions
```

## Deployment Options

### Option 1: Render (Recommended - Free Tier)

**`render.yaml`:**
```yaml
services:
  - type: web
    name: portfolio
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn run:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: FLASK_ENV
        value: production
```

### Option 2: Railway

Similar to Render, Railway auto-detects Python and Flask applications.

### Option 3: PythonAnywhere

Upload code, set up virtual environment in their dashboard, configure WSGI file.

### Option 4: Docker + Any Platform

**`Dockerfile`:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
```

## Development Workflow

### 1. Setup
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
```

### 2. Run Development Server
```bash
flask run --debug
# Or
python run.py
```

### 3. Run Tests
```bash
pytest                    # Run all tests
pytest --cov             # With coverage
pytest -v                # Verbose
pytest tests/test_routes.py  # Specific file
```

### 4. Code Quality
```bash
pylint app/              # Lint code
black app/               # Format code
```

## Performance & Optimization

### Template Caching
```python
app.config['TEMPLATES_AUTO_RELOAD'] = False  # Production
app.jinja_env.cache = {}  # Add template caching
```

### Asset Compression
```python
from flask_compress import Compress
Compress(app)
```

### Static File Serving
In production, use CDN or nginx for static files.

## Security Considerations

- CSRF protection for contact form
- Environment variables for sensitive data
- HTTPS enforced in production
- Input validation and sanitization
- Security headers via Flask-Talisman

## Next Steps

Proceed to:
1. [Python Development Roadmap](../planning/03-python-development-roadmap.md)
2. [Flask Application Setup Guide](../planning/04-flask-setup-guide.md)
3. Start building!
