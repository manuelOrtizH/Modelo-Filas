from django.shortcuts import render
from django.http import HttpResponse
#Si quieres importar un archivo de scripts, así, velos escribiendo en la línea 4:
#from simulator.scripts import archivoQueQuieresUsar, archivo2...
#En código se usa: archivo.function()

def home(request):
    return render(request, 'simulator/home.html')

# Create your views here.
