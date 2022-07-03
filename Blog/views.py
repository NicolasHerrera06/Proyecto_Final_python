from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from Blog.forms import UserRegistrationForm
from .models import Posteo
from .forms import ContactoForm, PostForm

# Create your views here.

def inicio(request):
    posteos = Posteo.objects.all()
    data = {
        'posteo': posteos
    }
    return render(request, 'Blog/inicio.html',data)


    #plantilla = loader.get_template('inicio.html')
    #documento = plantilla.render()

    #return HttpResponse(documento)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario,  password = contra)

            if user is not None:
                login(request , user)

                return render(request, "Blog/bienvenido.html" , {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "Blog/bienvenido.html" , {'mensaje':"Error, datos incorrectos"})

        else:
             return render(request, "Blog/bienvenido.html" , {'mensaje':"Error, formulario erroneo"})
    form = AuthenticationForm()

    return render(request , "Blog/login.html" , {'form':form})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Blog/bienvenido.html" , {'mensaje' : "Usuario Creado"})

    else:
        form = UserRegistrationForm()

    return render(request, "Blog/register.html" , {"form":form})

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    #validamos
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'Blog/contacto.html', data)

def agregar_post(request):
    
    data = {
        'form': PostForm()
    }
    #validamos
    if request.method == 'POST':
        formulario = PostForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Post guardado"
        else:
            data["form"] = formulario

    return render(request, 'Blog/post.html',data)

def listar_post(request):
    publicacion = Posteo.objects.all()

    data = {
        'publicacion': publicacion
    }
    
 
    return render(request, 'Blog/listar.html', data)

def modificar_post(request,id):

    publicacion = get_object_or_404(Posteo, id=id)

    data = {
        'form': PostForm(instance=publicacion)
    }
    #validamos
    if request.method == 'POST':
        formulario = PostForm(data=request.POST, instance=publicacion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente!")
            return redirect(to='listar_post')
        else:
            data["form"] = formulario

 
    return render(request, 'Blog/modificar.html',data)

def eliminar_post(request,id):

    publicacion = get_object_or_404(Posteo, id=id)
    publicacion.delete()
    messages.success(request, "Eliminado correctamente!")
    return redirect(to='listar_post')