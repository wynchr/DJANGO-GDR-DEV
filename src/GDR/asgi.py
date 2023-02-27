"""
=======================================================================================================================
.DESCRIPTION
    ASGI config for GDR project.

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    It exposes the ASGI callable as a module-level variable named ``application``.

    For more information on this file, see
    https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
=======================================================================================================================
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDR.settings')

application = get_asgi_application()
