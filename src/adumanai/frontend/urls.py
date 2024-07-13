from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post",views.push_data, name="push_data")
]