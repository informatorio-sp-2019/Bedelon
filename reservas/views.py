from django.shortcuts import render, redirect
from reservas.models import Aula, Reserva, Feriado
from reservas.forms import LoginForm, SearchForm, AulaForm, FeriadoForm, DocenteForm, BedelForm
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def aulas(request):
	aulas = Aula.objects.all()
	total = Aula.objects.all().count()

	return render(request, 'aulas.html', {'aulas': aulas, 'total': total})

def home(request):
	
	try:
		oUsuario = request.user.docente
		tipo = 'DOCENTE'
	except:	
		try:
			oUsuario = request.user.bedel
			tipo = 'BEDEL'
		except:
			oUsuario = request.user
			tipo = 'SUPERUSUARIO'
	finally:
		pass

	template = 'home.html'
	context = {'usuario':oUsuario,'tipo':tipo}
	return render(request, template,context)


def login(request):

	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('reservas:home'))

	if request.method == 'POST':
		username_post = request.POST['username']
		password_post = request.POST['password']
		user = authenticate(request, username=username_post, password=password_post)

		if user is not None:
			login_django(request, user)
			# import ipdb
			# ipdb.set_trace()		
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
#			return render(request, 'nueva_aula_ok.html',{'aula':aula})
			return redirect('aulas')
	else:
		form = AulaForm()
		return render(request, 'nueva_aula.html',{'form':form})

#Amigos mios queridos, si les salta un error al ingresar un feriado

def feriadito(request):
	feriados = Feriado.objects.all().order_by('fecha')

	if request.method == 'POST':
		form = FeriadoForm(request.POST)
		if form.is_valid():
			feriado = form.save()
#			return render(request, 'agregar_feriado_ok.html',{'feriado':feriado})
			return redirect('aulas')
	else:
		form = FeriadoForm()
		return render(request, 'agregar_feriado.html',{'form':form, 'feriados':feriados})

def docente(request):
	if request.method == 'POST':
		form = DocenteForm(request.POST)
		if form.is_valid():
			_docente = form.save(commit=False)
			_docente.set_password(_docente.password)
			_docente.save()

			return redirect('aulas')

	else:
		form = DocenteForm()
		return render(request, 'agregar_docente.html',{'form':form})


def bedel(request):
	if request.method == 'POST':
		form = BedelForm(request.POST)
		if form.is_valid():
			_bedel = form.save(commit=False)
			_bedel.set_password(_bedel.password)
			_bedel.save()

			return redirect('aulas')
		
	form = BedelForm()
	template = 'agregar_bedel.html'
	contexto =  {'form':form}
	return render(request, template,contexto)


