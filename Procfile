release: python manage.py migrate
web: gunicorn myanalyzer.wsgi --timeout 100 --log-file -
