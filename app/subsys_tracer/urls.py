from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('search-status/', views.search_status, name="search_status"),
    path('change-status/', views.change_status, name="change_status"),
    path('delete-people/', views.delete_people, name="delete_people")
]