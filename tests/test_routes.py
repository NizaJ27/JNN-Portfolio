"""Tests for business section routes"""
import pytest


class TestBusinessRoutes:
    """Test business section routes"""
    
    def test_business_index_route(self, client):
        """Test that business index route returns 200"""
        response = client.get('/business/')
        assert response.status_code == 200
    
    def test_business_index_content(self, client):
        """Test that business page contains expected content"""
        response = client.get('/business/')
        assert b'Business Professional' in response.data
        assert b'Core Competencies' in response.data
        assert b'Professional Experience' in response.data
    
    def test_business_skills_displayed(self, client):
        """Test that business skills are displayed"""
        response = client.get('/business/')
        assert b'Business Analysis' in response.data
        assert b'Project Management' in response.data
        assert b'Strategic Planning' in response.data
    
    def test_business_resume_route(self, client):
        """Test that resume route exists"""
        response = client.get('/business/resume')
        assert response.status_code == 200


class TestDeveloperRoutes:
    """Test developer section routes"""
    
    def test_developer_index_route(self, client):
        """Test that developer index route returns 200"""
        response = client.get('/developer/')
        assert response.status_code == 200
    
    def test_developer_index_content(self, client):
        """Test that developer page contains expected content"""
        response = client.get('/developer/')
        assert b'Web Developer' in response.data
        assert b'Technical Skills' in response.data
        assert b'Technologies &amp; Tools' in response.data or b'Technologies & Tools' in response.data
    
    def test_developer_skills_displayed(self, client):
        """Test that developer skills are displayed"""
        response = client.get('/developer/')
        assert b'Python' in response.data
        assert b'Flask' in response.data or b'Flask/Django' in response.data
        assert b'JavaScript' in response.data
    
    def test_developer_github_route(self, client):
        """Test that GitHub route exists"""
        response = client.get('/developer/github')
        assert response.status_code == 200


class TestProjectsRoutes:
    """Test projects section routes"""
    
    def test_projects_index_route(self, client):
        """Test that projects index route returns 200"""
        response = client.get('/projects/')
        assert response.status_code == 200
    
    def test_projects_index_content(self, client):
        """Test that projects page contains expected content"""
        response = client.get('/projects/')
        assert b'Project Portfolio' in response.data
        assert b'AI Therapy Application' in response.data
        assert b'FastAPI Calculator' in response.data
    
    def test_projects_filter_all(self, client):
        """Test projects filter with 'all' category"""
        response = client.get('/projects/?category=all')
        assert response.status_code == 200
        assert b'AI Therapy Application' in response.data
    
    def test_projects_filter_backend(self, client):
        """Test projects filter with 'Backend' category"""
        response = client.get('/projects/?category=Backend')
        assert response.status_code == 200
        # Should show FastAPI Calculator which is Backend
        assert b'FastAPI Calculator' in response.data
    
    def test_projects_filter_fullstack(self, client):
        """Test projects filter with 'Full Stack' category"""
        response = client.get('/projects/?category=Full Stack')
        assert response.status_code == 200
        # Should show therapy app which is Full Stack
        assert b'AI Therapy Application' in response.data
    
    def test_project_detail_route(self, client):
        """Test that project detail route works"""
        response = client.get('/projects/therapy-app')
        assert response.status_code == 200
    
    def test_project_detail_therapy_app(self, client):
        """Test therapy app detail page content"""
        response = client.get('/projects/therapy-app')
        assert response.status_code == 200
        assert b'AI Therapy Application' in response.data
        assert b'OpenAI' in response.data
        assert b'tapp.theratoast.com' in response.data
    
    def test_project_detail_module14(self, client):
        """Test module14 detail page content"""
        response = client.get('/projects/module14')
        assert response.status_code == 200
        assert b'FastAPI Calculator with JWT Auth' in response.data
        assert b'PostgreSQL' in response.data
        assert b'calc.theratoast.com' in response.data
    
    def test_project_detail_portfolio(self, client):
        """Test portfolio detail page content"""
        response = client.get('/projects/portfolio')
        assert response.status_code == 200
        assert b'Personal Portfolio' in response.data
        assert b'100% test coverage' in response.data
    
    def test_project_detail_invalid_id(self, client):
        """Test that invalid project ID redirects to projects page"""
        response = client.get('/projects/nonexistent-project')
        assert response.status_code == 200
        # Should show projects page
        assert b'Project Portfolio' in response.data


class TestContactRoutes:
    """Test contact section routes"""
    
    def test_contact_get_route(self, client):
        """Test that contact form page loads"""
        response = client.get('/contact/')
        assert response.status_code == 200
        assert b'Get In Touch' in response.data
        assert b'Send Me a Message' in response.data
    
    def test_contact_form_displayed(self, client):
        """Test that contact form fields are present"""
        response = client.get('/contact/')
        assert b'name="name"' in response.data
        assert b'name="email"' in response.data
        assert b'name="subject"' in response.data
        assert b'name="message"' in response.data
    
    def test_contact_post_success(self, client):
        """Test successful form submission"""
        response = client.post('/contact/', data={
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message content'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b'Thank you for your message' in response.data
    
    def test_contact_post_missing_name(self, client):
        """Test form submission with missing name"""
        response = client.post('/contact/', data={
            'name': '',
            'email': 'test@example.com',
            'message': 'Test message'
        })
        assert response.status_code == 200
        assert b'Name is required' in response.data
    
    def test_contact_post_missing_email(self, client):
        """Test form submission with missing email"""
        response = client.post('/contact/', data={
            'name': 'Test User',
            'email': '',
            'message': 'Test message'
        })
        assert response.status_code == 200
        assert b'Valid email is required' in response.data
    
    def test_contact_post_invalid_email(self, client):
        """Test form submission with invalid email"""
        response = client.post('/contact/', data={
            'name': 'Test User',
            'email': 'invalid-email',
            'message': 'Test message'
        })
        assert response.status_code == 200
        assert b'Valid email is required' in response.data
    
    def test_contact_post_missing_message(self, client):
        """Test form submission with missing message"""
        response = client.post('/contact/', data={
            'name': 'Test User',
            'email': 'test@example.com',
            'message': ''
        })
        assert response.status_code == 200
        assert b'Message is required' in response.data
