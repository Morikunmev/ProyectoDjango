from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login #metodo login
from django.contrib.auth.forms import UserCreationForm
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

