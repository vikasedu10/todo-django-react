from django.urls import path
from api import views
from django.views.generic import RedirectView

urlpatterns = [
    path('api/notes/', views.getNotes, name="notes"),
    path('api/notes/<str:pk>/', views.getNote, name="note"),

    path('', RedirectView.as_view(url="api/notes/", permanent=True)),
]