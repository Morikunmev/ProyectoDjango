from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages #libreria que gestiona los erroeres

# Create your views here.
class VRegistro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            usuario = form.save()  # Guarda el nuevo usuario
            login(request, usuario)  # Inicia sesión al usuario
            return redirect('Home')  # Redirige a la página principal
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')  # Redirige a la página principal

def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username= nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Nombre de Usuario o Contraseña incorrectos")
        else:
            messages.error(request,"informacion incorrecta")
    
    
    form = AuthenticationForm()
    return render(request, "login/login.html", {'form': form})
