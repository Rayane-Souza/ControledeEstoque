# 
# projeto_controle_de_estoque/urls.py
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Redireciona a URL vazia para as URLs do app 'home'
    path('produtos/', include('produtos.urls')),  # Inclui as URLs do app 'produtos'
]
