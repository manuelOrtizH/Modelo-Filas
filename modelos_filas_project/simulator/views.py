from django.shortcuts import render
from django.http import HttpResponse
from simulator import model as m
# Create your views here.

def home(request):
    return render(request, 'simulator/home.html')

def input(request):
    name_model = request.GET.get('name_model')
    results = {'name_model': name_model, 'validation_msg': ''}
    return render(request, 'simulator/input.html', results)

def mm1Results(request):
    name_model = request.GET.get('name_model')
    data = m.Model(name_model, int(request.GET.get('l')), 
        int(request.GET.get('miu')), int(request.GET.get('n')), request.GET.get('time'))
    results = {'model': data.model, 'name_model': name_model}
    return render(request, 'simulator/mm1_results.html', results)

def mmsResults(request):
    name_model = request.GET.get('name_model')
    data = m.Model(name_model, int(request.GET.get('l')), int(request.GET.get('miu')), 
    int(request.GET.get('s')), int(request.GET.get('n')), request.GET.get('time'))
    results = {'model': data.model, 'name_model': name_model}
    return render(request, 'simulator/mms_results.html', results)

def mmskResults(request):
    name_model = request.GET.get('name_model')
    data = m.Model(name_model, int(request.GET.get('l')), int(request.GET.get('miu')), 
    int(request.GET.get('s')), int(request.GET.get('k')), int(request.GET.get('n')),
    request.GET.get('time'))
    results = {'model': data.model, 'name_model': name_model}
    return render(request, 'simulator/mmsk_results.html', results)

def mg1Results(request):
    name_model = request.GET.get('name_model')
    data = m.Model(name_model, int(request.GET.get('l')), 
    int(request.GET.get('miu')), int(request.GET.get('variance')), 
    int(request.GET.get('n')), request.GET.get('time'))
    results = {'model': data.model, 'name_model': name_model}
    return render(request, 'simulator/mg1_results.html', results)

