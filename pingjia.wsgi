import os
import sys

project_path = '/home/readll/pingjia'
if project_path not in sys.path:
    sys.path.append(project_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'pingjia.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
