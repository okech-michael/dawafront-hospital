import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_project.settings')

# Mark that we're running on Vercel for settings.py
if 'vercel' in os.environ.get('VERCEL_ENV', '').lower() or os.path.exists('/var/task'):
    os.environ['VERCEL'] = '1'

# Run migrations on startup
try:
    call_command('migrate', '--noinput', verbosity=0)
except Exception as e:
    print(f"Migration error (non-critical): {e}", file=sys.stderr)

# Get WSGI application
app = get_wsgi_application()

# Wrap with WhiteNoise for static file serving
from whitenoise import WhiteNoise
application = WhiteNoise(app)
