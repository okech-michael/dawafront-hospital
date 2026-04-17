# Dawafront Healthcare Website - Deployment Guide for Railway

This Django project is configured for deployment on Railway.app. Follow these steps to deploy:

## Prerequisites
- Railway.app account (https://railway.app)
- GitHub account with this repository

## Deployment Steps

### 1. Connect GitHub Repository
- Go to https://railway.app
- Click "New Project"
- Select "Deploy from GitHub"
- Connect your GitHub account
- Select the `dawafront-hospital` repository

### 2. Configure Environment Variables
Railway will automatically detect the Procfile and requirements.txt. Add these environment variables in the Railway dashboard:

```
SECRET_KEY=your-very-secure-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.railway.app,localhost
```

### 3. Database Setup
Railway automatically provisions a PostgreSQL database. The `DATABASE_URL` environment variable will be set automatically.

To migrate the database:
- The `release` command in Procfile runs migrations automatically on each deployment
- Or manually run: `railway run python manage.py migrate`

### 4. Collect Static Files
Static files are collected automatically during the build process through WhiteNoise.

### 5. Deploy
Once the environment variables are set, Railway will automatically deploy your application.

## Post-Deployment

### Create Superuser (Django Admin)
```bash
railway run python manage.py createsuperuser
```

### Access Your Site
- Main site: `https://yourdomain.railway.app`
- Admin panel: `https://yourdomain.railway.app/admin`

## Project Structure
```
project/
├── hospital_project/          # Django project settings
│   ├── settings.py           # Production-ready configuration
│   ├── urls.py
│   └── wsgi.py
├── main_app/                 # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/            # HTML templates
│   └── static/               # CSS, JS, images
├── manage.py
├── Procfile                  # Railway deployment config
├── runtime.txt               # Python version
├── requirements.txt          # Dependencies
└── .env.example             # Example environment variables
```

## Tech Stack
- **Framework**: Django 4.2
- **Database**: PostgreSQL (on Railway)
- **Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Frontend**: HTML5, CSS3, JavaScript

## Important Notes
- `DEBUG` is set to `False` in production (set via environment variable)
- Static files are served by WhiteNoise
- Database migrations run automatically on each deployment
- Media files should be stored in a persistent volume or external service (AWS S3, etc.)

## Troubleshooting
- Check Railway logs: `railway logs`
- Run specific commands: `railway run python manage.py [command]`
- SSH into container: `railway shell`

For more info, visit: https://docs.railway.app
