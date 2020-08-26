from django.urls import path
from . import views

urlpatterns = [
    path("", views.Search, name="homepage"),
]
