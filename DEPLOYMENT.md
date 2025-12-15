# JNN Portfolio - Deployment Guide

## Overview

This Flask portfolio uses automated CI/CD deployment with:

1. **Docker Hub** - Container image storage
2. **GitHub Actions** - Automated testing, building, and pushing
3. **Watchtower** - Automatic deployment on your server
4. **Gunicorn** - Production WSGI server

**Repository:** https://github.com/NizaJ27/JNN-Portfolio.git

---

## Architecture

```
Developer Flow:
┌─────────────────────────────────────────────────────────────┐
│ 1. Push code to GitHub (main branch)                         │
│    ↓                                                          │
│ 2. GitHub Actions triggers                                   │
│    ├─ Run pytest with 100% coverage                         │
│    ├─ Build Docker image                                    │
│    └─ Push to Docker Hub (nizaj27/jnn-portfolio)            │
│                                                               │
│ 3. Watchtower on server                                      │
│    ├─ Detects new image (every 5 minutes)                   │
│    ├─ Pulls latest image                                    │
│    ├─ Stops old container                                   │
│    └─ Starts new container                                  │
│                                                               │
│ 4. Portfolio is live! ✅                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## Prerequisites

- ✅ GitHub repository: `NizaJ27/JNN-Portfolio`
- ✅ Docker Hub account
- ✅ Server with Docker installed
- ✅ Domain name (optional)
- ✅ 100% test coverage locally

---

## Step 1: Docker Hub Setup

### Create Docker Hub Repository

1. Go to https://hub.docker.com
2. Click "Create Repository"
3. Configure:
   - **Name:** `jnn-portfolio`
   - **Visibility:** Public (free)
   - **Description:** "Personal portfolio - Business Analyst & Web Developer"

### Generate Access Token

1. Go to **Account Settings** > **Security**
2. Click "New Access Token"
3. Configure:
   - **Description:** `github-actions-jnn-portfolio`
   - **Permissions:** Read & Write
4. Copy token: `dckr_pat_xxxxxxxxxxxxx`

⚠️ **Save this token securely - you won't see it again!**

---

## Step 2: GitHub Secrets Configuration

Go to your GitHub repository: https://github.com/NizaJ27/JNN-Portfolio

**Settings** > **Secrets and variables** > **Actions** > **New repository secret**

Add these secrets:

| Secret Name | Value | Description |
|------------|-------|-------------|
| `DOCKER_USERNAME` | `nizaj27` | Your Docker Hub username |
| `DOCKER_TOKEN` | `dckr_pat_xxxxx` | Access token from Step 1 |
| `DOCKER_IMAGE` | `nizaj27/jnn-portfolio` | Full image name |

---

## Step 3: Test Locally with Docker

### Build and Run

```bash
cd /Users/joshuanizamudin/Desktop/NJIT\ 2025\ Fall/IS\ 218/Portfolio

# Build Docker image
docker build -t nizaj27/jnn-portfolio:latest .

# Run container
docker run -d \
  --name portfolio \
  -p 5000:5000 \
  -e SECRET_KEY="your-secret-key-here" \
  nizaj27/jnn-portfolio:latest

# Check logs
docker logs portfolio

# Test in browser
open http://localhost:5000
```

### Verify Endpoints

- ✅ `http://localhost:5000/` - Landing page
- ✅ `http://localhost:5000/business/` - Business section
- ✅ `http://localhost:5000/developer/` - Developer section
- ✅ `http://localhost:5000/projects/` - Projects
- ✅ `http://localhost:5000/contact/` - Contact form

### Stop and Clean Up

```bash
docker stop portfolio
docker rm portfolio
```

---

## Step 4: Deploy to Production

### Push to GitHub

```bash
# Check current status
git status

# Add all changes
git add .

# Commit with descriptive message
git commit -m "Add Docker deployment configuration with CI/CD"

# Push to main branch (triggers GitHub Actions)
git push origin main
```

### Monitor GitHub Actions

1. Go to: https://github.com/NizaJ27/JNN-Portfolio/actions
2. Watch the workflow run:
   - ✅ **Test** - Runs pytest with coverage
   - ✅ **Build and Push** - Creates Docker image
   - ✅ **Deploy Notification** - Confirms success

### Expected Output

```
✅ All tests passed (36 tests, 100% coverage)
✅ Docker image built successfully
✅ Image pushed to Docker Hub: nizaj27/jnn-portfolio:latest
🚀 Watchtower will auto-deploy on your server
```

---

## Step 5: Server Setup with Watchtower

### SSH to Your Server

```bash
ssh your-username@your-server-ip
```

### Create Environment File

```bash
# Create environment file for secrets
nano ~/.env.portfolio

# Add these variables:
SECRET_KEY=your-super-secret-key-change-this
FLASK_ENV=production
```

### Set Up with Docker Compose

```bash
# Create project directory
mkdir -p ~/portfolio
cd ~/portfolio

# Download docker-compose.yml from repository
curl -O https://raw.githubusercontent.com/NizaJ27/JNN-Portfolio/main/docker-compose.yml

# Start the application
docker compose --env-file ~/.env.portfolio up -d

# Verify it's running
docker compose ps
```

### Install Watchtower

```bash
# Run Watchtower for automatic updates
docker run -d \
  --name watchtower \
  --restart unless-stopped \
  -v /var/run/docker.sock:/var/run/docker.sock \
  containrrr/watchtower \
  --cleanup \
  --interval 300 \
  --label-enable

# Verify Watchtower is running
docker logs watchtower
```

**Watchtower will now:**
- Check Docker Hub every 5 minutes
- Pull new images when available
- Update your portfolio automatically
- Remove old images

---

## Step 6: Configure Nginx (Optional)

### Install Nginx

```bash
sudo apt update
sudo apt install nginx -y
```

### Create Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/portfolio
```

Add this configuration:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Enable and Restart

```bash
# Enable the site
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled/

# Test configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
```

### SSL with Certbot (Recommended)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Certbot will automatically configure HTTPS
```

---

## Deployment Workflow

### For Updates

```bash
# Make changes to your code
# Tests will run automatically when you push

# Commit and push
git add .
git commit -m "Update portfolio feature"
git push origin main

# Within 5-10 minutes:
# ✅ Tests pass on GitHub Actions
# ✅ Docker image builds and pushes
# ✅ Watchtower detects update
# ✅ Portfolio updates automatically
```

### Rollback (if needed)

```bash
# On your server
cd ~/portfolio

# Pull previous version (replace with actual tag)
docker pull nizaj27/jnn-portfolio:main-abc1234

# Update docker-compose.yml to use specific tag
# Then restart
docker compose up -d
```

### View Logs

```bash
# View application logs
docker compose logs -f web

# View Watchtower logs
docker logs -f watchtower

# View Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

---

## Monitoring

### Check Application Health

```bash
# Check if container is running
docker compose ps

# Health check
curl http://localhost:5000

# View resource usage
docker stats
```

### GitHub Actions Badge

Add to your README.md:

```markdown
![Deploy Status](https://github.com/NizaJ27/JNN-Portfolio/actions/workflows/deploy.yml/badge.svg)
```

---

## Troubleshooting

### Tests Fail on GitHub Actions

```bash
# Run tests locally first
pytest -v --cov=app

# Fix any failing tests
# Commit and push again
```

### Docker Build Fails

```bash
# Test build locally
docker build -t test-portfolio .

# Check Dockerfile syntax
# Verify all files are committed
```

### Watchtower Not Updating

```bash
# Check Watchtower logs
docker logs watchtower

# Manually update
docker compose pull
docker compose up -d
```

### Container Won't Start

```bash
# Check logs
docker compose logs web

# Verify environment variables
docker compose config

# Test locally
docker run -it nizaj27/jnn-portfolio:latest sh
```

---

## Security Best Practices

1. **Never commit secrets** - Use environment variables
2. **Use strong SECRET_KEY** - Generate with `python -c "import secrets; print(secrets.token_hex(32))"`
3. **Keep dependencies updated** - Regular `pip install --upgrade`
4. **Enable HTTPS** - Use Certbot/Let's Encrypt
5. **Firewall configuration** - Only allow ports 80, 443, 22
6. **Regular backups** - Backup your .env files

---

## Costs

- ✅ **GitHub Actions**: Free for public repositories (2,000 minutes/month)
- ✅ **Docker Hub**: Free for public images
- ✅ **Server**: ~$5-10/month (Digital Ocean, Linode, etc.)
- ✅ **Domain**: ~$10-15/year
- ✅ **SSL Certificate**: Free (Let's Encrypt)

**Total: ~$5-10/month + domain**

---

## Next Steps

1. ✅ Set up Docker Hub repository
2. ✅ Add GitHub secrets
3. ✅ Test Docker build locally
4. ✅ Push to GitHub to trigger deployment
5. ✅ Set up server with Watchtower
6. ✅ Configure domain and SSL
7. ✅ Add custom content (projects, resume, etc.)
8. ✅ Share your portfolio!

---

## Resources

- **Repository**: https://github.com/NizaJ27/JNN-Portfolio
- **Docker Hub**: https://hub.docker.com/r/nizaj27/jnn-portfolio
- **Docker Documentation**: https://docs.docker.com
- **GitHub Actions**: https://docs.github.com/en/actions
- **Watchtower**: https://containrrr.dev/watchtower/
- **Gunicorn**: https://gunicorn.org/

---

**Questions?** Open an issue on GitHub or contact jnizamudin@gmail.com
