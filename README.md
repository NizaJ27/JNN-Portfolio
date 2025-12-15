# Joshua Nizamudin - Portfolio

![Deploy Status](https://github.com/NizaJ27/JNN-Portfolio/actions/workflows/deploy.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0.0-green.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)

> A multi-faceted personal portfolio showcasing business analysis and web development skills

## 🎯 Features

- ✅ **100% Test Coverage** - 36 comprehensive tests with pytest
- ✅ **Multi-Section Portfolio** - Business, Developer, Projects, Contact pages
- ✅ **Responsive Design** - Mobile-first with Tailwind CSS
- ✅ **CI/CD Pipeline** - Automated deployment with GitHub Actions + Docker
- ✅ **Production Ready** - Gunicorn WSGI server, containerized with Docker

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/NizaJ27/JNN-Portfolio.git
cd JNN-Portfolio

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements-dev.txt

# Run tests (100% coverage)
pytest -v --cov=app

# Start development server
python run.py
# Visit http://localhost:5000
```

## 🐳 Docker Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete deployment guide using Docker Hub + GitHub Actions + Watchtower.

```bash
# Build Docker image
docker build -t nizaj27/jnn-portfolio .

# Run container
docker run -d -p 5000:5000 -e SECRET_KEY="your-key" nizaj27/jnn-portfolio
```

## Tech Stack

- HTML/CSS/JavaScript
- Modern web development practices
- Responsive design

## Contact

**Joshua Nizamudin**

- GitHub: [@NizaJ27](https://github.com/NizaJ27)
- Email: jnizamudin@gmail.com

---

Built with care by Joshua Nizamudin
