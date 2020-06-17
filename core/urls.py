from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('inicio/', HomePageView.as_view(template_name="home.html"), name="inicio"),
    path('visualizar/', View.as_view(), name="visualizar"),
    path('lista/', PersonList.as_view(), name="lista"),
    path('detalhe/<int:pk>', PersonDetail.as_view(), name="detalhe"),
    path('criar/', PersonCreate.as_view(), name="criar"),
    path('atualizar/<int:pk>', PersonUpdate.as_view(), name="atualizar"),
    path('deletar/<int:pk>', PersonDelete.as_view(), name="deletar"),
    path('dashboard/', Dashboard.as_view(), name="dashboard")
]
