from django import forms
from reservas.models import Aula, Feriado



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
