from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

from .models import Cliente, Main

class Principal(TemplateView):
	template_name="principal.html"
	context_object_name = 'principal'


class ListaCliente(ListView):
    """ vista para listar libros por autor """
    template_name = 'lista-clientes.html'
    context_object_name = 'cliente'

    def get_queryset(self):
        # identificar el autor
        #id = self.kwargs['pk']
        # filtro de los libros
        lista = Cliente.objects.filter()
        # devuelvo el resultado o la lista resultado
        return lista


class ListaMain(ListView):
    """ vista para listar libros por autor """
    template_name = 'lista-main.html'
    context_object_name = 'main'

    def get_queryset(self):
        # identificar el autor
        #id = self.kwargs['pk']
        # filtro de los libros
        lista = Main.objects.filter()
        # devuelvo el resultado o la lista resultado
        return lista


# Create your views here.
