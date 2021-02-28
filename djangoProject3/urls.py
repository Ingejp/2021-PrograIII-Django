"""djangoProject3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from djangoProject3.Views.HomeView import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('menu/', HomeView.menu, name='menu'),
    path('ruta2/<int:parametro1>', HomeView.ruta2, name='ruta2'),
    path('ruta3/<int:parametro1>/<int:parametro2>', HomeView.ruta3, name='ruta3'),
    path('formulario/', HomeView.formularioAlumno, name='formularioAlumno'),

]
