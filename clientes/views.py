from django.shortcuts import render,render_to_response, redirect
from clientes.forms import  ClienteForm, MainForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
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

        lista = Main.objects.filter()
        # devuelvo el resultado o la lista resultado
        return lista

def new_client(request):
    if request.method == "POST":

        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaCliente')
    else:
        form = ClienteForm()
    return render(request,'cliente.html',{'form':form})

def new_main(request):
    if request.method == "POST":

        form = MainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaMain')
    else:
        form = MainForm()
    return render(request,'main.html',{'form':form})


# Create your views here.
