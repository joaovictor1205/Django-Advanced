from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView
from .views import HomePageView, View, PersonList, PersonDetail, PersonCreate

urlpatterns = [
    path('inicio/', HomePageView.as_view(template_name="home.html"), name="inicio"),
    path('visualizar/', View.as_view(), name="visualizar"),
    path('lista/', PersonList.as_view(), name="lista"),
    path('detalhe/<int:pk>', PersonDetail.as_view(), name="detalhe"),
    path('criar/', PersonCreate.as_view(), name="criar"),
    
]
