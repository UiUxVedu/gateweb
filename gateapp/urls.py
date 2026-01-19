from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.add_application, name='apply'),

    # INFO PAGES
    path('info/cs/', views.info_cs, name='info_cs'),
    path('info/entc/', views.info_entc, name='info_entc'),
    path('info/elec/', views.info_elec, name='info_elec'),
    path('info/mech/', views.info_mech, name='info_mech'),

    # ADMIN ONLY
    path('applications/', views.application_list, name='application_list'),
]
