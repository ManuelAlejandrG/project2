from django import forms
from clientes.models import Cliente, Main

class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'

class MainForm(forms.ModelForm):
	class Meta:
		model = Main
		fields = '__all__'
