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
    # This will be populated from JSON later
    project = {
        'id': project_id,
        'title': 'Project Title',
        'description': 'Detailed project description...',
        'tags': ['Python', 'Flask'],
        'category': 'Full Stack'
    }
    
    return render_template(
        'pages/project_detail.html',
        title=f'{project["title"]} | Joshua Nizamudin',
        project=project
    )
