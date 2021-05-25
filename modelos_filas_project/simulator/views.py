from django.shortcuts import render
from django.http import HttpResponse
from simulator import model as m
from simulator import evaluate as e
# Create your views here.

def home(request):
    return render(request, 'simulator/home.html')

def input(request):
    name_model = request.GET.get('name_model')
    results = {'name_model': name_model, 'validation_msg': ''}
    return render(request, 'simulator/input.html', results)

def modelResults(request):
    name_model = request.GET.get('name_model')
    data = e.getModel(request, name_model)       
    results = {'model': data.model, 'name_model': name_model}
    return render(request, 'simulator/modelResults.html', results)