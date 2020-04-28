from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.utils import timezone
from django.urls import reverse_lazy

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = timezone.now()
        return context

class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('lista')

class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('lista')

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('lista')
