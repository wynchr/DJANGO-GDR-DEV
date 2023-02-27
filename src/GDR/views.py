"""
=======================================================================================================================
.DESCRIPTION
    Views for GDR Project

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from django.contrib.auth import authenticate, login, logout     # Logon / Logout authenticate
from django.contrib.auth.decorators import login_required       # Login required
from django.views.decorators.cache import cache_control         # Destroy tthe section after logout

# ================================================================================================================
# INFO containing settings for pages
# ================================================================================================================

INFO = settings.INFO_APPS


# =========================================================================================================
# INDEX & ADMINISTRATION & LOGIN/LOGOUT
# =========================================================================================================

# ===== INDEX =========

@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def gdr_index(request):
    context = {'info': INFO}
    return render(request, "GDR/gdr-index.html", context)

# ===== LOGIN/LOGOUT =========


# Login Function
def Login(request):
    context = {'info': INFO}
    if request.user is None or request.user == "" or request.user.username == "":
        return render(request, "GDR/login.html", context)
    else:
        return HttpResponseRedirect('/')


# Login User
def LoginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Enter your data correctly.")
            return  HttpResponseRedirect('/')


# Logout Function
def LogoutUser(request):
    logout(request)
    request.user = None
    return HttpResponseRedirect('/')

# EOF ---------------------------------------------------------------
