"""
WSGI config for zinkov_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import dj_database_url
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zinkov_backend.settings')

application = get_wsgi_application()

app = application