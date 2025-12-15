"""Contact page routes"""
from flask import Blueprint, render_template, request, flash, redirect, url_for

bp = Blueprint('contact', __name__, url_prefix='/contact')


@bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Contact form page
    
    Returns:
        Rendered template for contact page
    """
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Basic validation
        errors = []
        if not name:
            errors.append('Name is required')
        if not email or '@' not in email:
            errors.append('Valid email is required')
        if not message:
            errors.append('Message is required')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template(
                'pages/contact.html',
                title='Contact | Joshua Nizamudin',
                name=name,
                email=email,
                subject=subject,
                message=message
            )
        
        # TODO: Actually send email or save to database
        # For now, just show success message
        flash(f'Thank you for your message, {name}! I will get back to you soon.', 'success')
        return redirect(url_for('contact.index'))
    
    # GET request - show form
    return render_template(
        'pages/contact.html',
        title='Contact | Joshua Nizamudin'
    )
