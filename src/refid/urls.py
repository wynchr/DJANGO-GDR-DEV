"""
=======================================================================================================================
.DESCRIPTION
    list routes URLs to views for REFID Application

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
from django.urls import path
from .views import *

urlpatterns = [

    # =========================================================================================================
    # INDEX & INFORMATION
    # =========================================================================================================

    path('',
         refid_index,
         name="refid-index"),  # Entry Point for REFID

    path('readme/',
         refid_info_readme,
         name='refid-info-readme'),

    path('todo/',
         refid_info_todo,
         name='refid-info-todo'),

    path('about/',
         refid_info_about,
         name='refid-info-about'),




    # =========================================================================================================
    # APPLICATION
    # =========================================================================================================

    path('application/',
         RefidProvAdListView.as_view(),
         name='refid-application'),

    # ProvAd ==========

    path('provad-list-view/',
         RefidProvAdListView.as_view(),
         name="refid-provad-list-view"),

    path('provad-create-view/',
         RefidProvAdCreateView.as_view(),
         name='refid-provad-create-view'),

    path('provad-update-view/<str:pk>/',
         RefidProvAdUpdateView.as_view(),
         name='refid-provad-update-view'),

    # ProvInitAd ==========

    path('provinitad-list-view/',
         RefidProvInitAdListView.as_view(),
         name="refid-provinitad-list-view"),

    path('provinitad-create-view/',
         RefidProvInitAdCreateView.as_view(),
         name='refid-provinitad-create-view'),

    path('provinitad-update-view/<str:pk>/',
         RefidProvInitAdUpdateView.as_view(),
         name='refid-provinitad-update-view'),

    # ================================================================================================================
    # MONITORING
    # ================================================================================================================

    path('monitor-list-view/',
         RefidMonitorListView.as_view(),
         name='refid-monitor-list-view'),

    path('monitor-detail-view/<str:pk>/',
         RefidMonitorDetailView.as_view(),
         name='refid-monitor-detail-view'),

    path('monitor-compare/',
         refid_monitor_compare,
         name='refid-monitor-compare'),
    path('monitor-log/',
         refid_monitor_log,
         name='refid-monitor-log'),

    # =========================================================================================================
    # CACHE
    # =========================================================================================================

    # Cache RH ==========

    path('cacherh-list-view/',
         RefidCacheRHListView.as_view(),
         name='refid-cacherh-list-view'),

    path('cacherh-detail-view/<str:pk>/',
         RefidCacheRHDetailView.as_view(),
         name='refid-cacherh-detail-view'),

    # Cache AD ==========

    path('cachead-list-view/',
         RefidCacheADListView.as_view(),
         name='refid-cachead-list-view'),

    path('cachead-detail-view/<str:pk>/',
         RefidCacheADDetailView.as_view(),
         name='refid-cachead-detail-view'),

    # Cache EVIDIAN ==========

    path('cacheevidian-list-view/',
         RefidCacheEVIDIANListView.as_view(),
         name='refid-cacheevidian-list-view'),

    path('cacheevidian-detail-view/<str:pk>/',
         RefidCacheEVIDIANDetailView.as_view(),
         name='refid-cacheevidian-detail-view'),

    # =========================================================================================================
    # GENERATE PDF
    # =========================================================================================================


    path('refid_info_pdf/<str:RefidIopProvAd_id>/',
         refid_info_pdf,
         name='refid_info_pdf'),


    # =========================================================================================================
    # TESTS
    # =========================================================================================================

]

# =========================================================================================================
# No more used (hold in case)
# =========================================================================================================

# path('provad-create/', refid_provad_create, name="refid-provad-create"),     # Create Prov Entry

# path('monitor-list/', refid_monitor_list, name='refid-monitor-list'),
# path('monitor-detail/<str:RefidIopProvAd_id>/', refid_monitor_detail, name='refid-monitor-detail'),

# path('testform/', refid_test_form, name="refid-test-form"),  # Test fictive FORM

# path('test-home-view/',
#      TestView.as_view(title="View"),
#      name='test-home-view'),
# path('test-about-view/',
#      TestView.as_view(title="About"),
#      name='test-about-view'),
#
# path('test-template-view/',
#      TestTemplateView.as_view(title="Accueil du site"),
#      name='test-template-home-view'),
#
# path('test-template-about-view/',
#      TestTemplateView.as_view(title="A propos"),
#      name='test-template-about-view'),

# path('search/',
#      refid_search,
#      name='refid-search'),
#
# path('refid-search-view/',
#      SearchView.as_view(),
#      name='refid-search-view'),

# path('markdown/',
#      test_markdown_view,
#      name='test-markdown-view'),
