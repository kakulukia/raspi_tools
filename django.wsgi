import os
import sys

sys.path.append('/home/andy/projects/raspie_tools/')
sys.path.append('/home/andy/.virtualenvs/raspie_tools/lib/python2.7/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'raspie_tools.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
