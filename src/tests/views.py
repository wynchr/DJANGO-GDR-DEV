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
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings

from subprocess import Popen, PIPE

from .forms import SignupForm

INFO = settings.INFO_APPS


@login_required
def index(request):
    context = {'info': INFO}
    return render(request, "tests/index.html", context)

@login_required
def testhtml5(request):
    context = {'info': INFO}
    return render(request, "tests/testhtml5.html", context)


@login_required
def testbt5(request):
    context = {'info': INFO}
    return render(request, "tests/testbt5.html", context)


@login_required
def testbt5form(request):
    context = {'info': INFO}
    return render(request, "tests/testbt5form.html", context)


@login_required
def testbt5grid(request):
    context = {'info': INFO}
    return render(request, "tests/testbt5grid.html", context)


@login_required
def testtabs(request):
    context = {'info': INFO}
    return render(request, "tests/testtabs.html", context)


@login_required
def testsignup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # return HttpResponse("Merci de vous être inscrit au site.")
    else:
        form = SignupForm()

    return render(request, "tests/signup.html", {"form": form})


@login_required
def testtimeout(request):
    context = {'info': INFO}
    return render(request, "tests/testtimeout.html", context)


@login_required
def runscript(request):
    process = Popen(['python', '/HOME/DEV/DJANGO-GDR/src/utils/update_provinitad_ALL.py'], stdout=PIPE)
    output, error = process.communicate()

    return render(request, 'tests/script_output.html', {'output': output})