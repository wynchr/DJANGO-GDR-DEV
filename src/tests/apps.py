"""
=======================================================================================================================
.DESCRIPTION
    Test for TEST Application

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
from django.apps import AppConfig


class TestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tests'
