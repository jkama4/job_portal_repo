from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("", views.mars_images_view, name="mars_images_view"),
]