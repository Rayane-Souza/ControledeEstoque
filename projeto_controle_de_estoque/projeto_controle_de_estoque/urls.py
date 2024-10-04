# 
# projeto_controle_de_estoque/urls.py
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  
    path('produtos/', include('produtos.urls')),  
]
