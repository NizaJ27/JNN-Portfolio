"""Projects section routes"""
from flask import Blueprint, render_template, request

bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/')
def index():
    """
    Projects portfolio page with filtering
    
    Returns:
        Rendered template for projects section
    """
    # Sample projects data - will be replaced with JSON data later
    projects = [
        {
            'id': 'therapy-app',
            'title': 'AI Therapy Application',
            'description': 'Mental health support app with AI-powered chatbot using OpenAI API',
            'tags': ['Python', 'Flask', 'OpenAI', 'Healthcare'],
            'category': 'Full Stack',
            'image': '/static/images/projects/therapy-app.jpg',
            'github': 'https://github.com/NizaJ27/IS218-AI-Demo',
            'demo': 'https://tapp.theratoast.com',
            'featured': True
        },
        {
            'id': 'module14',
            'title': 'FastAPI Calculator with JWT Auth',
            'description': 'Advanced web application with JWT authentication, PostgreSQL database, and calculation BREAD operations',
            'tags': ['Python', 'FastAPI', 'PostgreSQL', 'JWT', 'CI/CD'],
            'category': 'Backend',
            'image': '/static/images/projects/module14.jpg',
            'github': 'https://github.com/NizaJ27/IS218-Module-14',
            'demo': 'https://calc.theratoast.com',
            'featured': True
        },
        {
            'id': 'portfolio',
            'title': 'Personal Portfolio',
            'description': 'This portfolio website built with Flask, Python, and TDD methodology',
            'tags': ['Python', 'Flask', 'Tailwind CSS', 'Pytest'],
            'category': 'Full Stack',
            'image': '/static/images/projects/portfolio.jpg',
            'github': 'https://github.com/NizaJ27/Portfolio',
            'demo': None,
            'featured': False
        }
    ]
    
    # Get filter from query params
    category_filter = request.args.get('category', 'all')
    
    # Filter projects if needed
    if category_filter != 'all':
        projects = [p for p in projects if p['category'] == category_filter]
    
    categories = ['All', 'Full Stack', 'Frontend', 'Backend', 'Data Science']
    
    return render_template(
        'pages/projects.html',
        title='Projects | Joshua Nizamudin',
        projects=projects,
        categories=categories,
        active_category=category_filter
    )


@bp.route('/<project_id>')
def detail(project_id):
    """
    Individual project detail page
    
    Args:
        project_id: Project identifier
        
    Returns:
        Rendered template for project detail
    """
    # Comprehensive project data
    project_data = {
        'therapy-app': {
            'id': 'therapy-app',
            'title': 'AI Therapy Application',
            'category': 'Full Stack',
            'description': 'Mental health support app with AI-powered chatbot using OpenAI API',
            'tags': ['Python', 'Flask', 'OpenAI', 'Healthcare', 'AI', 'REST API'],
            'github': 'https://github.com/NizaJ27/IS218-AI-Demo',
            'demo': 'https://tapp.theratoast.com',
            'problem_statement': 'Mental health support is often inaccessible due to cost, availability, and stigma. Many individuals need immediate support but face barriers in accessing professional help. This project addresses the need for an accessible, private, and immediate mental health support tool.',
            'features': [
                'AI-powered conversational therapy chatbot using OpenAI GPT-4',
                'Secure user authentication and session management',
                'Real-time chat interface with contextual understanding',
                'Privacy-focused architecture with encrypted conversations',
                'Responsive design for mobile and desktop access',
                'Sentiment analysis for monitoring user emotional state'
            ],
            'technical_implementation': 'Built with Flask backend integrated with OpenAI API for natural language processing. Implements RESTful API architecture for chat interactions. Uses session management for conversation context and user data protection.',
            'technologies': {
                'Frontend': 'HTML5, CSS3, Tailwind CSS, JavaScript',
                'Backend': 'Python, Flask, OpenAI API',
                'Testing': 'pytest, unittest, API mocking',
                'Deployment': 'Docker, Caddy, Digital Ocean'
            },
            'challenges': 'Key challenges included managing API rate limits, maintaining conversation context across sessions, ensuring user privacy, and creating a natural conversational flow. Implemented caching strategies, session state management, and robust error handling to address these issues.',
            'results': 'Successfully deployed application providing 24/7 mental health support access. Maintains conversation context across sessions with low latency responses. Positive user feedback on conversational quality and accessibility.'
        },
        'module14': {
            'id': 'module14',
            'title': 'FastAPI Calculator with JWT Auth',
            'category': 'Backend',
            'description': 'Advanced web application with JWT authentication, PostgreSQL database, and calculation BREAD operations',
            'tags': ['Python', 'FastAPI', 'PostgreSQL', 'JWT', 'Docker', 'CI/CD'],
            'github': 'https://github.com/NizaJ27/IS218-Module-14',
            'demo': 'https://calc.theratoast.com',
            'problem_statement': 'Modern web applications require secure user authentication, persistent data storage, and full CRUD operations. This project demonstrates enterprise-grade backend development with FastAPI, implementing secure JWT authentication and comprehensive calculation history management.',
            'features': [
                'JWT-based authentication with access and refresh tokens',
                'Complete BREAD operations (Browse, Read, Edit, Add, Delete) for calculations',
                'PostgreSQL database with SQLAlchemy ORM',
                'User registration and login with password hashing',
                'Calculation history tracking per user',
                'RESTful API with OpenAPI/Swagger documentation',
                'Comprehensive pytest test suite with 100% coverage',
                'CI/CD pipeline with GitHub Actions'
            ],
            'technical_implementation': 'Built with FastAPI framework for high-performance API endpoints. Uses SQLAlchemy for database ORM with PostgreSQL backend. Implements secure password hashing with bcrypt and JWT token management. Follows TDD methodology with comprehensive test coverage.',
            'technologies': {
                'Backend': 'Python, FastAPI, SQLAlchemy, Pydantic',
                'Database': 'PostgreSQL, Alembic migrations',
                'Security': 'JWT, bcrypt, python-jose',
                'Testing': 'pytest, pytest-cov, httpx',
                'DevOps': 'Docker, GitHub Actions, Watchtower'
            },
            'challenges': 'Implementing secure JWT token refresh flow, managing database migrations, ensuring test isolation with fixtures, and handling concurrent user sessions. Solved through comprehensive security testing, proper fixture scoping, and transaction management.',
            'results': 'Production-ready API with 100% test coverage deployed with automated CI/CD. Handles multiple concurrent users with secure authentication. Comprehensive API documentation via OpenAPI. Successfully demonstrates enterprise backend development practices.'
        },
        'portfolio': {
            'id': 'portfolio',
            'title': 'Personal Portfolio',
            'category': 'Full Stack',
            'description': 'This portfolio website built with Flask, Python, and TDD methodology',
            'tags': ['Python', 'Flask', 'Tailwind CSS', 'Pytest', 'Docker', 'TDD'],
            'github': 'https://github.com/NizaJ27/JNN-Portfolio',
            'demo': 'https://theratoast.com',
            'problem_statement': 'Professional developers need a compelling portfolio to showcase their work, skills, and experience. This portfolio demonstrates full-stack development capabilities, testing methodology, and modern DevOps practices while maintaining clean, maintainable code.',
            'features': [
                'Multi-page Flask application with Blueprint routing',
                'Responsive design with Tailwind CSS',
                '100% test coverage with 36 comprehensive tests',
                'Featured projects showcase with live demos',
                'Business and developer personas highlighting dual expertise',
                'Contact form with professional inquiry handling',
                'Dockerized deployment with automated CI/CD',
                'HTTPS with automatic SSL certificate management'
            ],
            'technical_implementation': 'Built using Flask application factory pattern with Blueprint-based routing for modularity. Implements comprehensive pytest test suite following TDD methodology. Uses Jinja2 templating with Tailwind CSS for responsive design. Deployed with Docker, GitHub Actions, and Watchtower for continuous deployment.',
            'technologies': {
                'Backend': 'Python 3.13, Flask 3.0, Jinja2',
                'Frontend': 'Tailwind CSS, Alpine.js, HTML5',
                'Testing': 'pytest, pytest-cov, pytest-flask',
                'DevOps': 'Docker, GitHub Actions, Caddy, Watchtower',
                'Quality': 'pylint, black, 100% test coverage'
            },
            'challenges': 'Achieving 100% test coverage, implementing efficient CI/CD pipeline, managing multiple domain configurations with Caddy, and ensuring zero-downtime deployments. Addressed through comprehensive test strategy, proper Docker networking, and automated deployment workflows.',
            'results': 'Professional portfolio with 100% test coverage successfully deployed at theratoast.com. Automated CI/CD pipeline ensures all tests pass before deployment. Zero-downtime updates via Watchtower. Demonstrates both technical skills and professional presentation.'
        }
    }
    
    # Get project data or return 404
    project = project_data.get(project_id)
    if not project:
        # Return to projects page if project not found
        return render_template(
            'pages/projects.html',
            title='Projects | Joshua Nizamudin',
            projects=list(project_data.values()),
            categories=['All', 'Full Stack', 'Frontend', 'Backend', 'Data Science'],
            active_category='all'
        )
    
    return render_template(
        'pages/project_detail.html',
        title=f'{project["title"]} | Joshua Nizamudin',
        project=project
    )
