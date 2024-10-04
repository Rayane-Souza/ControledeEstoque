from django.urls import path
from .views import my_login_view  

urlpatterns = [
    path('login/', my_login_view, name='login'),  
]
