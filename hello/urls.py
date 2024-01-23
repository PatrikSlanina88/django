from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jebat/", views.jebat, name="jebat"),
    path("nevim/", views.nevim, name="nevim")
]
