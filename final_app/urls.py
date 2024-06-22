# myapp/urls.py
from django.urls import path
from . import views
from typing import List, Any
from django.contrib.auth import views as auth_views

urlpatterns: List[Any] = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("results/", views.results, name="results"),
    path("error/", views.error, name="error"),
]
