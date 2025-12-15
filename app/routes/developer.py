"""Developer section routes"""
from flask import Blueprint, render_template

bp = Blueprint('developer', __name__, url_prefix='/developer')


@bp.route('/')
def index():
    """
    Developer section landing page
    
    Returns:
        Rendered template for developer section
    """
    # Sample developer data - will be replaced with JSON data later
    skills = [
        {'name': 'Python', 'level': 90, 'category': 'Backend'},
        {'name': 'Flask/Django', 'level': 85, 'category': 'Backend'},
        {'name': 'JavaScript', 'level': 80, 'category': 'Frontend'},
        {'name': 'HTML/CSS', 'level': 88, 'category': 'Frontend'},
        {'name': 'SQL/PostgreSQL', 'level': 82, 'category': 'Database'},
        {'name': 'Git/GitHub', 'level': 87, 'category': 'Tools'},
        {'name': 'REST APIs', 'level': 85, 'category': 'Backend'},
        {'name': 'Testing (pytest)', 'level': 88, 'category': 'Quality'}
    ]
    
    technologies = {
        'Languages': ['Python', 'JavaScript', 'HTML/CSS', 'SQL'],
        'Frameworks': ['Flask', 'Django', 'Tailwind CSS', 'Alpine.js'],
        'Tools': ['Git', 'VS Code', 'Docker', 'Pytest'],
        'Databases': ['PostgreSQL', 'SQLite', 'MongoDB']
    }
    
    return render_template(
        'pages/developer.html',
        title='Web Developer | Joshua Nizamudin',
        skills=skills,
        technologies=technologies
    )


@bp.route('/github')
def github():
    """
    GitHub profile and contributions
    
    Returns:
        Rendered template for GitHub showcase
    """
    return render_template(
        'pages/github.html',
        title='GitHub Profile | Joshua Nizamudin'
    )
