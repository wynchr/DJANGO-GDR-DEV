"""
=======================================================================================================================
.DESCRIPTION
    list routes URLs to views for GDR Project

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/4.1/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
=======================================================================================================================
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [

    # =========================================================================================================
    # INDEX & ADMINISTRATION & LOGIN/LOGOUT
    # =========================================================================================================

    # ===== INDEX =========

    path('', gdr_index, name="gdr-index"),

    # ===== ADMINISTRATION =========

    path('gdr-admin/', admin.site.urls),

    # ===== LOGIN/LOGOUT =========

    path('login/', Login, name="login"),
    path('login_user', LoginUser, name="login_user"),
    path('logout/', LogoutUser, name="logout"),

    # =========================================================================================================
    # APPLICATION
    # =========================================================================================================

    path('refid/', include('refid.urls')),

    # =========================================================================================================
    # TESTS
    # =========================================================================================================

    path('tests/', include('tests.urls')),

]

# =========================================================================================================
# ADD LOGIC
# =========================================================================================================

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ================================================================================================================
# Function Handle Errors pages
# ================================================================================================================

handler500 = 'refid.views.error_500'
handler404 = 'refid.views.error_404'

# =========================================================================================================
# No more used (hold in case)
# =========================================================================================================

# path('',home,name="home"),