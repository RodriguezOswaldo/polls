from django.urls import path

from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("luke/", views.luke, name="luke"),
    path("arthur/", views.arthur, name="arthur"),
]
