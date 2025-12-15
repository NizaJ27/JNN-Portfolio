"""Pytest configuration and fixtures"""
import pytest
from app import create_app


@pytest.fixture
def app():
    """
    Create Flask application for testing
    
    Returns:
        Flask application configured for testing
    """
    app = create_app('testing')
    return app


@pytest.fixture
def client(app):
    """
    Create test client
    
    Args:
        app: Flask application fixture
        
    Returns:
        Test client for making requests
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """
    Create test CLI runner
    
    Args:
        app: Flask application fixture
        
    Returns:
        CLI runner for testing commands
    """
    return app.test_cli_runner()
