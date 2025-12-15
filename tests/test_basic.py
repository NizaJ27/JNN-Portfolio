"""Basic application tests"""
import pytest
from app import create_app


class TestApplicationFactory:
    """Test application creation and configuration"""
    
    def test_config(self):
        """Test that testing configuration is applied"""
        assert not create_app('development').testing
        assert create_app('testing').testing
    
    def test_app_exists(self, app):
        """Test that application exists"""
        assert app is not None
    
    def test_app_is_testing(self, app):
        """Test that app is in testing mode"""
        assert app.config['TESTING']


class TestRoutes:
    """Test basic routes"""
    
    def test_index_route(self, client):
        """Test that index route returns 200"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_index_content(self, client):
        """Test that index route contains expected content"""
        response = client.get('/')
        assert b'Joshua Nizamudin' in response.data
        assert b'Business Strategist' in response.data
        assert b'Web Developer' in response.data
    
    def test_about_route(self, client):
        """Test that about route returns 200"""
        response = client.get('/about')
        assert response.status_code == 200
        assert b'About page coming soon!' in response.data
    
    def test_404_error(self, client):
        """Test that 404 error is handled"""
        response = client.get('/nonexistent-page')
        assert response.status_code == 404
        assert b'Page not found' in response.data


class TestTemplates:
    """Test template rendering"""
    
    def test_base_template_loads(self, client):
        """Test that base template loads with Tailwind CSS"""
        response = client.get('/')
        assert b'tailwindcss' in response.data
        assert b'alpinejs' in response.data
    
    def test_navigation_component(self, client):
        """Test that navigation component is present"""
        response = client.get('/')
        assert b'<nav' in response.data
        assert b'Home' in response.data
    
    def test_footer_component(self, client):
        """Test that footer component is present"""
        response = client.get('/')
        assert b'<footer' in response.data
        assert b'Joshua Nizamudin' in response.data
        assert b'jnizamudin@gmail.com' in response.data


class TestErrorHandlers:
    """Test error handler functionality"""
    
    def test_500_error_handler(self, app):
        """Test that 500 error handler is registered"""
        # This tests that the error handler exists
        assert app.error_handler_spec[None][500] is not None
    
    def test_404_error_handler(self, app):
        """Test that 404 error handler is registered"""
        # This tests that the error handler exists
        assert app.error_handler_spec[None][404] is not None


class TestConfiguration:
    """Test application configuration"""
    
    def test_secret_key_set_in_testing(self, app):
        """Test that SECRET_KEY is set in testing mode"""
        assert app.config['SECRET_KEY'] is not None
        assert len(app.config['SECRET_KEY']) > 0
    
    def test_config_without_secret_key(self):
        """Test that app sets SECRET_KEY if config doesn't have one"""
        from app.config import Config
        # Temporarily remove SECRET_KEY from config
        original_key = Config.SECRET_KEY
        Config.SECRET_KEY = None
        
        app = create_app('testing')
        # App should set a default SECRET_KEY
        assert 'SECRET_KEY' in app.config
        assert app.config['SECRET_KEY'] is not None
        
        # Restore original
        Config.SECRET_KEY = original_key
