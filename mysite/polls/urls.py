from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("luke/", views.luke, name="luke"),
    path("arthur/", views.arthur, name="arthur"),
]
