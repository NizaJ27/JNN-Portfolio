"""Main routes (landing page)"""
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """
    Landing page route
    
    Returns:
        Rendered template for landing page
    """
    return render_template(
        'pages/index.html',
        title='Joshua Nizamudin | Portfolio'
    )


@bp.route('/about')
def about():
    """
    About page route (placeholder for now)
    
    Returns:
        Simple about message
    """
    return "About page coming soon!"
