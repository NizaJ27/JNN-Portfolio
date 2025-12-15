"""Flask application factory"""
from flask import Flask
from app.config import config


def create_app(config_name='default'):
    """
    Create and configure Flask application
    
    Args:
        config_name: Configuration name (development, testing, production)
        
    Returns:
        Flask application instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Set a secret key for flash messages
    if not app.config.get('SECRET_KEY'):
        app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    
    # Register blueprints
    from app.routes import main, business, developer, projects, contact
    app.register_blueprint(main.bp)
    app.register_blueprint(business.bp)
    app.register_blueprint(developer.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(contact.bp)
    
    # Register error handlers
    register_error_handlers(app)
    
    return app


def register_error_handlers(app):
    """Register error handlers"""
    
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return "Page not found", 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        return "Internal server error", 500
