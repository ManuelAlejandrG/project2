from django.forms import Modelform
from django import forms
from clientes.models import Cliente, Main

class ClienteForm(forms.Form):
	class Meta:
		model = Cliente

class MainForm(forms.Form):
	class Meta:
		model = Main
		