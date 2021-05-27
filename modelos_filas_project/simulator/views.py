from django.shortcuts import render
from django.http import HttpResponse
from simulator import model as m
from simulator import evaluate as e
from simulator import validations as v
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

    if name_model == 'MMS' or name_model == 'MMSK':
        if not v.validateServer(data.model.s): 
            del data
            return render(request, 'simulator/input.html', {'name_model': name_model, 'validation_msg': 'Error: El servidor debe ser mayor a 1'})

    if not v.validateNegatives([data.model.l, data.model.miu, data.model.s, data.model.k, data.model.variance, data.model.n, data.model.cw, data.model.cs]):
        del data
        return render(request, 'simulator/input.html', {'name_model': name_model, 'validation_msg': 'Error: Hay algún valor negativo'})

    if not v.validateLambda(data.model.l, data.model.s, data.model.miu):
        d = data.model.s * data.model.miu
        message = f'Error: λ es mayor a {d} ' 
        del data
        return render(request, 'simulator/input.html', {'name_model': name_model, 'validation_msg': message})


    results = {'model': data.model, 'name_model': name_model}
    return render(request, 'simulator/modelResults.html', results)