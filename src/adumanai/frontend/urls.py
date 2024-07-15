from django.urls import path

from . import views

app_name = 'frontend'
urlpatterns = [
    path("", views.index, name="index"),
    path("forms_page", views.push_data_view, name="push_data_view"),
]