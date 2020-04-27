from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView
from .views import HomePageView, View, PersonList

urlpatterns = [
    path('home/', HomePageView.as_view(template_name="home.html"), name="home"),
    path('view/', View.as_view(), name="view"),
    path('list/', PersonList.as_view(), name="list"),
]
