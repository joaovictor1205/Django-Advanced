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

from django.db.models import Max, Min
from .models import *

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

    def get_success_url(self):
        return reverse_lazy('lista')

class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name']

    def get_success_url(self):
        return reverse_lazy('lista')

class PersonDelete(DeleteView):
    model = Person

    def get_success_url(self):
        return reverse_lazy('lista')

class Dashboard(View):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('core.ver_dashboard'):
            return HttpResponse('Acesso Negado!')
        return super(Dashboard, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        mais_pedido = Pedido.objects.all().aggregate(Max('quantidade'))['quantidade__max']
        menos_pedido = Pedido.objects.all().aggregate(Min('quantidade'))['quantidade__min']

        alterar_estoque = request.user.has_perm('core.change_estoque')

        qtd_pedidos = Pedido.objects.all().count()

        context = {
            'mais_pedido': mais_pedido,
            'menos_pedido': menos_pedido,
            'qtd_pedidos': qtd_pedidos,
            'alterar_estoque': alterar_estoque,
        }

        return render(request, 'dashboard.html', context)
