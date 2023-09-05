from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola),
    path('fecha/', views.fecha),
    path('render/', views.template),
    path('info/', views.info),
]
            