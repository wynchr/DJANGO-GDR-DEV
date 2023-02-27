"""
=======================================================================================================================
.DESCRIPTION
    Add REFID Application for Administration

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS

=======================================================================================================================
"""
from django.apps import AppConfig


class RefidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'refid'
