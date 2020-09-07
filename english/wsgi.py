"""
WSGI config for english project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/pi/Documents/Django/english')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'english.settings')
#referencia (en python) desde el path anterior al fichero settings.py
#Importante hacerlo así, si hay varias instancias coriendo (en lugar de setdefault)
os.environ['DJANGO_SETTINGS_MODULE'] = 'english.settings'
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyectodjango.settings')

#prevenimos UnicodeEncodeError
os.environ.setdefault('LANG', 'en_US.UTF-8')
os.environ.setdefault('LC_ALL', 'en_US.UTF-8')

#obtenemos la aplicación
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
