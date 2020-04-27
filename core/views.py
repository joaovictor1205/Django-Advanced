from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.views import View
from .models import Person

class HomePageView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context = {
            'teste': 'teste',
        }

        return context

class View(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST")

class PersonList(ListView):
    model = Person
