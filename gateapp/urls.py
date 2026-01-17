from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
    path('filter/', views.filter_details),
]
