# Python Flask Portfolio - Development Roadmap

## Project Timeline: 6-8 Weeks

Python/Flask development with TDD approach, testing at each step.

---

## Week 1: Project Setup & Foundation

### Objectives
- Set up Python virtual environment
- Initialize Flask project structure
- Configure testing framework
- Create base application skeleton

### Day 1: Environment Setup

**Tasks:**
```bash
# Create project directory
cd "/Users/joshuanizamudin/Desktop/NJIT 2025 Fall/IS 218/Portfolio"

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # Mac/Linux

# Upgrade pip
pip install --upgrade pip
```

- [ ] Create virtual environment
- [ ] Activate virtual environment
- [ ] Verify Python version (3.11+)
- [ ] Create `.gitignore` for Python

**Test:** `python --version` shows 3.11+

### Day 2: Install Dependencies

**Create `requirements.txt`:**
```txt
Flask==3.0.0
python-dotenv==1.0.0
gunicorn==21.2.0
Markdown==3.5.0
PyYAML==6.0.1
```

**Create `requirements-dev.txt`:**
```txt
-r requirements.txt
pytest==7.4.3
pytest-cov==4.1.0
pytest-flask==1.3.0
pylint==3.0.3
black==23.12.0
```

```bash
pip install -r requirements-dev.txt
```

- [ ] Install production dependencies
- [ ] Install development dependencies
- [ ] Verify installations with `pip list`

**Test:** `pytest --version` works

### Day 3: Project Structure

**Create directories and files:**
```bash
mkdir -p app/{routes,templates/{pages,components,errors},static/{css,js,images,files},models,utils}
mkdir -p content tests
touch run.py
touch app/__init__.py
touch app/config.py
touch pytest.ini
touch .env.example
```

- [ ] Create project structure
- [ ] Initialize `__init__.py` files
- [ ] Create basic configuration files
- [ ] Set up `.env.example`

**Test:** `ls -R` shows correct structure

### Day 4: Basic Flask App

**Create `run.py`:**
```python
"""Application entry point"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

**Create `app/__init__.py`:**
```python
"""Flask application factory"""
from flask import Flask

def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return "Portfolio Coming Soon!"
    
    return app
```

- [ ] Create application factory
- [ ] Create basic route
- [ ] Test Flask runs: `python run.py`
- [ ] Visit http://localhost:5000

**Test:** App runs and shows "Portfolio Coming Soon!"

### Day 5: Testing Setup

**Create `pytest.ini`:**
```ini
[pytest]
testpaths = tests
python_files = test_*.py
addopts = 
    --verbose
    --cov=app
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=70
```

**Create `tests/conftest.py`:**
```python
"""Pytest configuration and fixtures"""
import pytest
from app import create_app

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    """Test client"""
    return app.test_client()
```

**Create `tests/test_basic.py`:**
```python
"""Basic application tests"""

def test_app_exists(app):
    """Test app fixture works"""
    assert app is not None

def test_index_route(client):
    """Test index page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Portfolio' in response.data
```

- [ ] Configure pytest
- [ ] Create test fixtures
- [ ] Write first tests
- [ ] Run tests: `pytest`

**Test:** All tests pass ✓

### Deliverables Week 1
✅ Virtual environment set up  
✅ Flask application running  
✅ Testing framework configured  
✅ First tests passing  
✅ Project structure complete  

---

## Week 2: Configuration & Base Templates

### Objectives
- Set up configuration management
- Create base HTML templates
- Add Tailwind CSS
- Build navigation and footer components

### Day 1: Configuration

**Create `app/config.py`:**
```python
"""Application configuration"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True

class ProductionConfig(Config):
    """Production configuration"""
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

- [ ] Create configuration classes
- [ ] Set up environment variables
- [ ] Update app factory to use config
- [ ] Test configuration loading

**Test:** `pytest tests/test_config.py`

### Day 2: Base Template

**Create `app/templates/base.html`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Joshua Nizamudin{% endblock %}</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Alpine.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    
    <!-- Custom CSS -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body class="min-h-screen flex flex-col bg-gray-50">
    {% include 'components/navigation.html' %}
    
    <main class="flex-grow">
        {% block content %}{% endblock %}
    </main>
    
    {% include 'components/footer.html' %}
</body>
</html>
```

- [ ] Create base template
- [ ] Add Tailwind CSS via CDN
- [ ] Add Alpine.js for interactivity
- [ ] Test template renders

**Test:** View source shows Tailwind loaded

### Day 3: Navigation Component

**Create `app/templates/components/navigation.html`:**
```html
<nav class="bg-white shadow-sm sticky top-0 z-50" x-data="{ mobileMenuOpen: false }">
    <div class="container mx-auto px-4">
        <div class="flex justify-between items-center h-16">
            <!-- Logo -->
            <a href="{{ url_for('main.index') }}" class="text-2xl font-bold text-gray-900">
                JN
            </a>
            
            <!-- Desktop Navigation -->
            <div class="hidden md:flex space-x-8">
                <a href="{{ url_for('main.index') }}" 
                   class="text-gray-700 hover:text-blue-600 transition">
                    Home
                </a>
                <a href="{{ url_for('business.index') }}" 
                   class="text-gray-700 hover:text-blue-600 transition">
                    Business
                </a>
                <a href="{{ url_for('development.index') }}" 
                   class="text-gray-700 hover:text-blue-600 transition">
                    Development
                </a>
                <a href="{{ url_for('projects.index') }}" 
                   class="text-gray-700 hover:text-blue-600 transition">
                    Projects
                </a>
                <a href="{{ url_for('contact.index') }}" 
                   class="text-gray-700 hover:text-blue-600 transition">
                    Contact
                </a>
            </div>
            
            <!-- Mobile Menu Button -->
            <button @click="mobileMenuOpen = !mobileMenuOpen" 
                    class="md:hidden">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                          d="M4 6h16M4 12h16M4 18h16"/>
                </svg>
            </button>
        </div>
        
        <!-- Mobile Menu -->
        <div x-show="mobileMenuOpen" 
             x-transition 
             class="md:hidden py-4">
            <a href="{{ url_for('main.index') }}" 
               class="block py-2 text-gray-700 hover:text-blue-600">
                Home
            </a>
            <!-- Add other mobile links -->
        </div>
    </div>
</nav>
```

- [ ] Create navigation component
- [ ] Add mobile responsive menu
- [ ] Style with Tailwind
- [ ] Test navigation links

**Test:** Navigation renders and is clickable

### Day 4: Footer Component

**Create `app/templates/components/footer.html`:**
```html
<footer class="bg-gray-900 text-white py-12">
    <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Quick Links -->
            <div>
                <h3 class="text-lg font-semibold mb-4">Quick Links</h3>
                <ul class="space-y-2">
                    <li><a href="{{ url_for('main.index') }}" class="hover:text-blue-400">Home</a></li>
                    <li><a href="{{ url_for('business.index') }}" class="hover:text-blue-400">Business</a></li>
                    <li><a href="{{ url_for('development.index') }}" class="hover:text-blue-400">Development</a></li>
                    <li><a href="{{ url_for('projects.index') }}" class="hover:text-blue-400">Projects</a></li>
                </ul>
            </div>
            
            <!-- Social Links -->
            <div>
                <h3 class="text-lg font-semibold mb-4">Connect</h3>
                <div class="flex space-x-4">
                    <a href="https://github.com/NizaJ27" target="_blank" 
                       class="hover:text-blue-400">GitHub</a>
                    <a href="https://linkedin.com/in/joshuanizamudin" target="_blank" 
                       class="hover:text-blue-400">LinkedIn</a>
                    <a href="mailto:jnizamudin@gmail.com" 
                       class="hover:text-blue-400">Email</a>
                </div>
            </div>
            
            <!-- Copyright -->
            <div>
                <p class="text-gray-400">
                    © 2025 Joshua Nizamudin<br>
                    Built with Flask + Python
                </p>
            </div>
        </div>
    </div>
</footer>
```

- [ ] Create footer component
- [ ] Add social links
- [ ] Style with Tailwind
- [ ] Test footer renders

**Test:** Footer shows on all pages

### Day 5: Static Files & Custom CSS

**Create `app/static/css/main.css`:**
```css
/* Custom styles beyond Tailwind */

:root {
    --primary-blue: #2563eb;
    --primary-purple: #7c3aed;
}

/* Smooth scroll */
html {
    scroll-behavior: smooth;
}

/* Custom button hover effects */
.btn-primary {
    @apply px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold;
    @apply hover:bg-blue-700 transition-all duration-200;
    @apply hover:shadow-lg hover:-translate-y-0.5;
}

/* Card hover effects */
.card {
    @apply transition-all duration-300;
}

.card:hover {
    @apply shadow-xl -translate-y-1;
}
```

- [ ] Create custom CSS file
- [ ] Add CSS variables
- [ ] Add utility classes
- [ ] Test CSS loads

**Test:** Custom styles apply

### Deliverables Week 2
✅ Configuration management working  
✅ Base template structure  
✅ Navigation with mobile menu  
✅ Footer component  
✅ Tailwind CSS integrated  

---

## Week 3: Landing Page & Routing

### Objectives
- Set up Blueprint routing
- Create landing page
- Build hero section
- Add about section

### Day 1: Blueprint Setup

**Create `app/routes/__init__.py`:**
```python
"""Route blueprints"""
```

**Create `app/routes/main.py`:**
```python
"""Main routes (landing page)"""
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Landing page"""
    return render_template('pages/index.html',
                         title='Joshua Nizamudin | Portfolio')
```

**Update `app/__init__.py`:**
```python
def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main.bp)
    
    return app
```

- [ ] Create blueprint structure
- [ ] Register blueprints
- [ ] Create placeholder routes
- [ ] Test routes work

**Test:** `pytest tests/test_routes.py`

### Day 2-5: Landing Page Development

Continue with landing page, data loading, business section, etc.

Follow similar pattern:
1. Write tests first (TDD)
2. Implement feature
3. Run tests
4. Commit to Git

---

## Week 4-8: Continue Development

Following the same TDD approach for:
- Business section (Week 4)
- Developer section (Week 5)
- Projects section (Week 6)
- Contact form (Week 7)
- Deployment (Week 8)

---

## Testing Workflow (Every Feature)

```bash
# 1. Write test first
# tests/test_feature.py

# 2. Run test (should fail)
pytest tests/test_feature.py -v

# 3. Implement feature
# app/routes/feature.py

# 4. Run test again (should pass)
pytest tests/test_feature.py -v

# 5. Check coverage
pytest --cov=app --cov-report=term-missing

# 6. Lint code
pylint app/

# 7. Format code
black app/

# 8. Commit
git add .
git commit -m "feat: add feature"
```

---

## Deployment (Week 8)

### Render Deployment

1. **Create `requirements.txt` (freeze dependencies):**
```bash
pip freeze > requirements.txt
```

2. **Create `Procfile`:**
```
web: gunicorn run:app
```

3. **Push to GitHub**

4. **Deploy on Render:**
- Connect GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `gunicorn run:app`
- Deploy!

**Test:** Visit deployed URL

---

## Next Steps

Ready to start Week 1, Day 1? Let's begin! 🚀
