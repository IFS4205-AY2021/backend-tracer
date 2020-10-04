from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search-status/', views.search_status, name="search_status"),
    path('change-status/', views.change_status, name="change_status"),
    path('search-contact/', views.search_contact, name="search_contact"),
    path('add-contact/', views.add_contact, name="add_contact"),
    path('delete-contact/', views.delete_contact, name="delete_contact"),
    path('search-records/', views.search_records, name="search_records")
]