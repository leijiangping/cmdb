"""
WSGI config for sdj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sdj.settings")

# from django_websocket.wsgi import get_wsgi_websocket_application


application = get_wsgi_application()
# websocket = get_wsgi_websocket_application()
