from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lobby/', views.lobby, name='lobby'),
    path('upLoad/', views.upLoad, name='upLoad'),
    path('changePassword', views.changePassword, name='changePassword'),
]
