from django.urls import path
from .views import (
    note_list, note_create, note_update, note_delete
)

app_name = 'notes'

urlpatterns = [
    path('notes/', note_list, name='note_list'),
    path('notes/create/', note_create, name='note_create'),
    path('notes/<int:pk>/update/', note_update, name='note_update'),
    path('notes/<int:pk>/delete/', note_delete, name='note_delete'),
]