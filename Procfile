web: gunicorn hospital_project.wsgi --log-file -
release: python manage.py migrate && python manage.py collectstatic --noinput
