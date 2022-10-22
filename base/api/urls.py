from django.urls import path
from . import views


urlpatterns = [
    path('', views.allNotes),
    path('search_note/<str:pk>', views.searchNotes),
    path('create_note/',views.createNotes),
    path('update_note/<str:pk>/', views.updateNotes),
    path('delete_note/<str:pk>/', views.deleteNotes),
    path('note/<str:pk>/', views.viewNote),
]