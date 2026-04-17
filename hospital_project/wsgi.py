import os
import sys
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_project.settings')

# Run migrations on startup
try:
    call_command('migrate', '--noinput', verbosity=0)
except Exception as e:
    print(f"Migration error (non-critical): {e}", file=sys.stderr)

application = get_wsgi_application()
