from django.urls import path
from . import views
from .models import Note

urlpatterns = [
    
    path('notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>/', views.getNote, name="note"),
    path('notes/create', views.createNote, name="create-note"),
    path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),
]