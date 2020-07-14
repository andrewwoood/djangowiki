from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random_page, name = "random"),
    path("results", views.search, name = "search"),
    path("newEntry", views.newEntry, name = "newEntry"),
    path("<str:entryTitle>", views.load_entry, name = "loadEntry")
]
