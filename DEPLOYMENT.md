# Railway Deployment Guide

This guide covers how to deploy the Contact Manager application on Railway.

## Prerequisites

- Railway account (https://railway.app)
- GitHub repository with the Contact Manager code
- PostgreSQL database (Railway provides this)

## Step-by-Step Deployment

### 1. Prepare Your Code

Ensure your project has:
- ✅ `requirements.txt` (for local dev dependencies)
- ✅ `requirements-production.txt` (or use Railway's detection)
- ✅ `Procfile` (already included)
- ✅ `.env.example` (already included)
- ✅ `manage.py` (already included)

### 2. Push Code to GitHub

```bash
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 3. Create Railway Project

1. Visit https://railway.app
2. Sign in to your account
3. Click "Create a new project"
4. Select "Deploy from GitHub repo"
5. Connect your GitHub account and select the ContactList repository

### 4. Configure Environment Variables

In Railway dashboard, add the following environment variables:

#### Critical Settings
```
SECRET_KEY=your-very-long-random-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app-name.railway.app,www.your-app-name.railway.app
```

#### Database (Auto-Provided)
```
DATABASE_URL=postgresql://user:password@host:port/database
```
*Railway automatically provides this when you add PostgreSQL plugin*

#### Superuser Settings
```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=your-very-secure-password-here
```

### 5. Add PostgreSQL Database

1. In Railway dashboard, click "Add a Plugin"
2. Select "PostgreSQL"
3. Railway will automatically add `DATABASE_URL` environment variable

### 6. Deploy

1. Railway automatically deploys when you push to GitHub
2. Check deployment logs in Railway dashboard
3. The `Procfile` commands will execute:
   - Run migrations: `python manage.py migrate`
   - Create superuser: `python manage.py create_superuser`

### 7. Access Your Application

Once deployment is complete:
- Application URL: `https://your-app-name.railway.app`
- Admin Panel: `https://your-app-name.railway.app/admin/`

### 8. Create Superuser (If Needed)

If the automatic superuser creation fails, create manually via Railway:

1. Open "Deployments" in Railway dashboard
2. Click the deployment
3. Go to "Logs"
4. Enter this command in the shell:
```bash
python manage.py createsuperuser
```

## Environment Variables Reference

### Django Core Settings
| Variable | Value | Description |
|----------|-------|-------------|
| `SECRET_KEY` | Random string | Django secret key (generate a new one!) |
| `DEBUG` | `False` | Always False in production |
| `ALLOWED_HOSTS` | Your domain | Railway domain and any custom domains |

### Database
| Variable | Value | Description |
|----------|-------|-------------|
| `DATABASE_URL` | PostgreSQL URI | Auto-provided by Railway PostgreSQL plugin |

### Authentication
| Variable | Value | Description |
|----------|-------|-------------|
| `DJANGO_SUPERUSER_USERNAME` | admin | Admin username |
| `DJANGO_SUPERUSER_EMAIL` | admin@example.com | Admin email |
| `DJANGO_SUPERUSER_PASSWORD` | secure password | Admin password (change immediately!) |

## Security Best Practices

1. **Generate a strong SECRET_KEY**
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

2. **Use strong passwords**
   - Minimum 12 characters
   - Mix uppercase, lowercase, numbers, symbols

3. **Keep DATABASE_URL secret**
   - Never commit `.env` file
   - Only set in Railway environment variables

4. **Monitor logs**
   - Check Railway logs regularly for errors
   - Set up error notifications

5. **Use custom domain (optional)**
   - In Railway dashboard: Settings → Domain
   - Add your custom domain
   - Update `ALLOWED_HOSTS` environment variable

## Updating Your Application

### Deploy Changes

1. Make changes to your code
2. Commit and push to GitHub
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```
3. Railway automatically redeploys

### Run Database Migrations

For new migrations:
1. Run locally first: `python manage.py makemigrations && python manage.py migrate`
2. Commit migration files
3. Push to GitHub
4. Railway runs migrations automatically from `Procfile`

If you need to run migrations manually:
1. Open Railway deployment
2. Click "Open Shell"
3. Run: `python manage.py migrate`

## Monitoring & Maintenance

### Check Application Health
1. Go to Railway dashboard
2. Click your project
3. Monitor CPU, Memory usage
4. Check deployment logs for errors

### View Logs
1. Click "Deployments"
2. Select the deployment
3. View real-time logs
4. Search logs for errors

### Database Backups
Railway automatically backs up PostgreSQL databases. To restore:
1. Contact Railway support or use Railway dashboard
2. Backups are available in database settings

## Troubleshooting

### Application Won't Start
1. Check logs for errors
2. Verify all environment variables are set
3. Ensure `Procfile` syntax is correct
4. Check database connection string

### Static Files Not Loading
1. Ensure `STATIC_URL` is set correctly in `settings.py`
2. Collect static files: `python manage.py collectstatic`
3. Verify `STATIC_ROOT` is configured

### Database Connection Issues
1. Check `DATABASE_URL` is set
2. Verify PostgreSQL plugin is added
3. Check database credentials
4. Try restarting the application

### Migrations Not Running
1. Check `Procfile` for correct command
2. Verify migrations are committed to Git
3. Check logs for migration errors
4. Manually run: `python manage.py migrate`

### Superuser Not Created
1. Check environment variables are set
2. Verify `create_superuser` command in `Procfile`
3. Manually create: `python manage.py createsuperuser`

## Scale Your Application

### More Resources
1. In Railway dashboard: Settings → Sizing
2. Increase CPU and memory allocation
3. Apply changes

### Custom Domain
1. In Railway settings: Domains
2. Add custom domain
3. Update DNS records
4. Update `ALLOWED_HOSTS` in environment variables

## Cost Estimation

Railway provides generous free tier:
- 5GB RAM
- Public 8GB Disk
- PostgreSQL included
- Web Services
- Check https://railway.app/pricing for current rates

## Support & Resources

- Railway Docs: https://docs.railway.app/
- Railway Community: https://discord.gg/railway
- Django Docs: https://docs.djangoproject.com/
- PostgreSQL Docs: https://www.postgresql.org/docs/

## Advanced Configuration

### Custom Workers
If you need background tasks, add to `Procfile`:
```
worker: celery -A ContactList worker --loglevel=info
```

### Scheduled Tasks
Use Django Celery Beat:
```bash
pip install django-celery-beat
```

### Environment-Specific Settings
Create separate settings files:
- `settings/base.py` - Common settings
- `settings/development.py` - Development settings
- `settings/production.py` - Production settings

---

Your Contact Manager is now live on Railway! 🚀
