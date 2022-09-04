from django.urls import path
from . import views

app_name = 'meeting'

urlpatterns = [
    path('', views.lobby, name=''),
    path('room/', views.room, name='room'),
    path('supervisor_room/', views.supervisorRoom),
    path('get_token/', views.getToken),

    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    #path('getImageName/', views.getImageName, name='getImageName'),
]
