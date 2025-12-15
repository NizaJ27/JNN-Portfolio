"""Business section routes"""
from flask import Blueprint, render_template

bp = Blueprint('business', __name__, url_prefix='/business')


@bp.route('/')
def index():
    """
    Business section landing page
    
    Returns:
        Rendered template for business section
    """
    # Sample business data - will be replaced with JSON data later
    skills = [
        {'name': 'Business Analysis', 'level': 90},
        {'name': 'Project Management', 'level': 85},
        {'name': 'Strategic Planning', 'level': 88},
        {'name': 'Data Analysis', 'level': 85},
        {'name': 'Process Optimization', 'level': 80},
        {'name': 'Stakeholder Management', 'level': 87}
    ]
    
    experience = [
        {
            'title': 'Business Analyst Intern',
            'company': 'Tech Solutions Inc.',
            'period': '2023 - 2024',
            'description': 'Analyzed business processes and developed optimization strategies'
        },
        {
            'title': 'Project Coordinator',
            'company': 'Innovation Labs',
            'period': '2022 - 2023',
            'description': 'Coordinated cross-functional teams and managed project timelines'
        }
    ]
    
    return render_template(
        'pages/business.html',
        title='Business Professional | Joshua Nizamudin',
        skills=skills,
        experience=experience
    )


@bp.route('/resume')
def resume():
    """
    Resume/CV page
    
    Returns:
        Rendered template for resume
    """
    return render_template(
        'pages/resume.html',
        title='Resume | Joshua Nizamudin'
    )
