from django.shortcuts import render, HttpResponse
from .models import Project, User
from .forms import ProjectForm, PersonaForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

# Create your views here.
# vista basada en funcion para el home de las vistas
def home(request):
    return render(request, "core/home.html")

# funcion basada en vistas que retorna un template pasandole como parametros
# un json con los anuncios y la informacion correspondiente
def anuncios(request):
    projects = Project.objects.all()
    return render(request, "core/anuncios.html", {'projects':projects})

# funcion basada en vista que mediante metodo POST se agrega un anuncio
# tambien se renderiza un template retornado pasandole como parametro un json
def addanuncio(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return render(request,"core/home.html")
	else:
		form = ProjectForm()
	return render(request, 'core/addanuncio.html', {'form':form})

# funcion basada en vistas que se le pasa como parametro el id de el anuncio correspondiente
# a editar para luego renderizar un template pasandole como parametro un json
def anuncioedit(request, id_anuncio):
	anuncio = Project.objects.get(id = id_anuncio)
	if request.method == 'GET':
		form = ProjectForm(instance = anuncio)
	else:
		form = ProjectForm(request.POST, instance = anuncio)
		if form.is_valid():
			form.save()
		return render(request,"core/home.html")
	return render(request, 'core/addanuncio.html', {'form':form})

# funcion basada en vistas para eliminar un anuncio tambien recibe un parametro id
# como identificador del anuncio para luego consultarlo y eliminarlo
# finalmente renderizamos un template pasandole como parametro un json
def anunciodel(request, id_anuncio):
	anuncio = Project.objects.get(id = id_anuncio)
	if request.method == 'POST':
		anuncio.delete()
		return render(request,"core/anuncios.html")
	return render(request, 'core/anuncio_delete.html', {'anuncio':anuncio})

# funcion basada en vista para el login de usuario
def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse('home'))
	return render(request, 'core/index.html', {})


	






"""form = ProjectForm(request.POST or None)
if form.is_valid():
form.save()
return redirect('home')
return redirect('home')"""


