from django.urls import path
from . import views
from web import views

urlpatterns = [
    path("", views.index, name="index"),
     path('form',views.form, name='form'),
    ]