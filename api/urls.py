from django.urls import path
from api import views

urlpatterns = [
    path('', views.home, name="home"),
    path('api/notes/', views.getNotes, name="notes"),
    path('api/notes/<str:pk>/', views.getNote, name="note"),
]