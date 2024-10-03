from django.urls import path
from home import views


urlpatterns = [
    path('', views.login_view, name='login'),

]
