from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('view/<int:pk>', views.produto_view, name='produto_view'),
    path('new', views.produto_create, name='produto_new'),
    path('detail/<int:pk>', views.produto_view, name='produto_detail'),
    path('edit/<int:pk>', views.produto_update, name='produto_edit'),
    path('delete/<int:pk>', views.produto_delete, name='produto_delete'),
]

