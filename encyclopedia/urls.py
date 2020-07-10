from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entryTitle>", views.loadEntry, name = "loadEntry")
    # path("<str:name>", views.greet, name = "greet")

]
