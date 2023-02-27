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
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="tests-index"),

    path('testhtml5/', testhtml5, name="tests-testhtml5"),
    path('testbt5/', testbt5, name="tests-testbt5"),
    path('testbt5form/', testbt5form, name="tests-testbt5form"),
    path('testbt5grid/', testbt5grid, name="tests-testbt5grid"),

    path('testsignup/', testsignup, name="test-signup"),

    path('testtabs/', testtabs, name="tests-testtabs"),

    path('testtimeout/', testtimeout, name="tests-timeout"),

    path('runscript/', runscript, name="tests-runscript"),
]



