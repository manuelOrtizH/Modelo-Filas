"""modelos_filas_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from simulator import views

urlpatterns = [
    path('', views.home),
    path('input/', views.input, name='input'),
    path('mm1_results/', views.mm1Results, name='mm1_results'),
    path('mms_results/', views.mmsResults, name='mms_results'),
    path('mmsk_results/', views.mmskResults, name='mmsk_results'),
    path('mg1_results/', views.mg1Results, name='mg1_results'),
]
