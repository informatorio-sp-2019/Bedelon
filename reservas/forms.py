from django import forms
from reservas.models import Aula, Feriado, Docente, Bedel
from django.contrib.auth.models import User


class LoginForm(forms.Form):
	username = forms.CharField(max_length = 30)
	password = forms.CharField(max_length = 30, widget=forms.PasswordInput())


class SearchForm(forms.Form):
	fecha= forms.DateField(label='Desde cuando', required=False)


class AulaForm(forms.ModelForm):
	class Meta:
		model = Aula
		fields = ('nombre', 'plazas', 'tipo_pizarra', 'tipo_aula', 'ubicacion')


class FeriadoForm(forms.ModelForm):
	class Meta:
		model = Feriado
		fields = ('fecha', 'descripcion')


class DocenteForm(forms.ModelForm):
	password = forms.CharField(max_length=20, widget = forms.PasswordInput())

	class Meta:
		model = Docente
		fields = ('username','password','nombre','apellido')


class BedelForm(forms.ModelForm):

	class Meta:
		model = Bedel
		fields = ('username','password','nombre','apellido')
		widget = {'password':forms.PasswordInput()}
