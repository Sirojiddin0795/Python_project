from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('frameworks/', views.frameworks, name='frameworks'),
    path('libraries/', views.libraries, name='libraries'),
    path('documentation/', views.documentation, name='documentation'),
]
