"""
URL configuration for app_artemis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from web_artemis.views import index, novo_relato, disque_denuncia  # Corrigido
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),  # Página inicial
    path('novo-relato/', novo_relato, name='novo_relato'),  # Página de criação de relatos
    path('disque-denuncia/', disque_denuncia, name='disque_denuncia'),  # Página de disque denúncia
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Adiciona essa linha
]
