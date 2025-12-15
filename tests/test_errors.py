"""Test error handlers"""
import pytest
from werkzeug.exceptions import InternalServerError


def test_500_error_handler_directly(app):
    """Test the 500 error handler returns correct message"""
    with app.app_context():
        # Get the 500 error handler and invoke it directly
        handlers = app.error_handler_spec[None][500]
        # The handler is stored as a dict, get the first one
        handler_func = list(handlers.values())[0] if handlers else None
        
        if handler_func:
            # Call the handler with a test error
            response = handler_func(InternalServerError())
            assert "Internal server error" in str(response[0])
            assert response[1] == 500
