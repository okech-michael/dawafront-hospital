# Dawafront Healthcare Website - Vercel Deployment Guide

This Django project is now configured for deployment on Vercel. Follow these steps to deploy:

## Prerequisites
- Vercel account (https://vercel.com)
- GitHub account with this repository
- Node.js installed locally (for Vercel CLI)

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Connect GitHub**
   - Go to https://vercel.com/dashboard
   - Click "Add New" → "Project"
   - Select "Import Git Repository"
   - Search for and select `dawafront-hospital`
   - Click "Import"

2. **Configure Project Settings**
   - Framework Preset: Leave as "Other"
   - Root Directory: `project`
   - Build Command: Leave empty (uses vercel.json)
   - Output Directory: Leave empty

3. **Add Environment Variables**
   - Click "Environment Variables"
   - Add the following variables:
     ```
     SECRET_KEY=your-very-secure-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=your-domain.vercel.app,localhost,127.0.0.1
     ```

4. **Deploy**
   - Click "Deploy"
   - Vercel will build and deploy your application

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   cd project
   vercel
   ```

4. **Follow the prompts** to complete deployment

## Configuration Files

The following files support Vercel deployment:

- **vercel.json** - Vercel-specific configuration (builds, routes, environment)
- **build.sh** - Build script that collects static files and runs migrations
- **hospital_project/settings.py** - Django settings configured for production
- **hospital_project/wsgi.py** - WSGI application with auto-migrations

## Database Setup

### Using SQLite (Default)
The app uses SQLite by default. Database migrations run automatically during deployment.

### Using PostgreSQL (Recommended for Production)
1. Set up a PostgreSQL database (e.g., on Railway, AWS RDS, or Heroku)
2. Add `DATABASE_URL` environment variable to Vercel:
   ```
   DATABASE_URL=postgresql://user:password@host:port/database_name
   ```

## Static Files & Media

- Static files are automatically collected during build using WhiteNoise
- Media files are stored in the `/media` directory
- For production, consider using cloud storage (AWS S3, Cloudinary, etc.)

## Environment Variables for Production

Add these to Vercel dashboard:

```
SECRET_KEY=<generate-a-strong-secret-key>
DEBUG=False
ALLOWED_HOSTS=your-domain.vercel.app
CSRF_TRUSTED_ORIGINS=https://your-domain.vercel.app,https://*.vercel.app
```

## Post-Deployment

### Create Superuser (Django Admin)
Use Vercel's environment variables or create via Django shell:

```bash
vercel env pull .env.local
python manage.py createsuperuser
```

### Access Your Site
- Main site: `https://your-domain.vercel.app`
- Admin panel: `https://your-domain.vercel.app/admin`

## Troubleshooting

### Static Files Not Loading
- Ensure `STATIC_ROOT` is set correctly in settings.py
- Check that WhiteNoise middleware is enabled
- Verify vercel.json includes static files route

### Database Migrations Failed
- Check the Vercel deployment logs
- Ensure migrations directory exists
- Verify DATABASE_URL environment variable is set correctly

### Import Errors
- Ensure all packages in requirements.txt are installed
- Check Python version compatibility (3.11+)

## Redeploying

To redeploy after making changes:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Vercel will automatically redeploy when you push to GitHub.

## Resources

- [Vercel Django Guide](https://vercel.com/docs/frameworks/django)
- [Vercel Documentation](https://vercel.com/docs)
- [Django Documentation](https://docs.djangoproject.com)
