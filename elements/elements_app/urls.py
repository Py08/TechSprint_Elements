from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
import django

urlpatterns = [
    path("", views.home, name="home"),
    path("festival_info/", views.festival_info, name = "festival-info"),
    path("performances/", views.performances, name = "performances"),
    path("tickets/", views.tickets, name = "tickets"),
]
