from django.urls import path

from . import views

urlpatterns = [
    path('rooms', views.rooms, name='roomlists'),
    path('<slug:slug>/', views.room, name='room')
    ]