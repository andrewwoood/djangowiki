from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random_page, name = "random"),
    path("<str:entryTitle>", views.load_entry, name = "loadEntry")
]
