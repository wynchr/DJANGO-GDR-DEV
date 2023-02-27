"""
=======================================================================================================================
.DESCRIPTION
    WSGI config for GDR project.

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    It exposes the WSGI callable as a module-level variable named ``application``.

    For more information on this file, see
    https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
=======================================================================================================================
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDR.settings')

application = get_wsgi_application()

# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
