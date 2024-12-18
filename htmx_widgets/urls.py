from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search, name="search"),
    path("add_item", views.add_item, name="add_item"),
]
