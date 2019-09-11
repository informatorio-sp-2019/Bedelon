from django.shortcuts import render
from reservas.models import Aula, Reserva
from django.shortcuts import render, redirect
from reservas.forms import LoginForm, SearchForm, AulaForm
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def aulas(request):
	aulas = Aula.objects.all()
	total = Aula.objects.all().count()

	return render(request, 'aulas.html', {'aulas': aulas, 'total': total})

def home(request):
	template = 'home.html'
	return render(request, template)


def login(request):

	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('reservas:home'))

	if request.method == 'POST':
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate(request, username=username_post, password=password_post)

		if user is not None:
			login_django(request, user)
			return HttpResponseRedirect(reverse('reservas:home'))
	
	form = LoginForm()

	context = {'form': form}
	template = 'login.html'

	return render(request, template, context)

def logout(request):
	logout_django(request)
	return HttpResponseRedirect(reverse('reservas:login'))


def fechas_reservas(request,id):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			fecha = form.cleaned_data ['fecha']
			aula = Aula.objects.get(pk=id)
			reservas = Reserva.objects.filter(fecha=fecha, aula=aula)

			return render(request, 'reservas.html', {'fecha':fecha, 'aula':aula,'reservas': reservas})
	else:
		form = SearchForm()
		return render(request, 'seleccionar_fecha.html',{'form':form, 'id': id})

def nuevaaula(request):
	if request.method == 'POST':
		form = AulaForm(request.POST)
		if form.is_valid():
			aula = form.save()
			return render(request, 'nueva_aula_ok.html',{'aula':aula})
	else:
		form = AulaForm()
		return render(request, 'nueva_aula.html',{'form':form})