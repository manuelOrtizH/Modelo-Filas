from simulator import model as m

def getModel(request, name_model):
    cw = float(request.GET.get('cw'))
    cs = float(request.GET.get('cs'))
    if name_model == 'MM1':
        return m.Model(name_model, float(request.GET.get('l')), 
               float(request.GET.get('miu')), int(request.GET.get('n')), request.GET.get('time'), cw, cs)
    elif name_model == 'MMS':
        return m.Model(name_model, float(request.GET.get('l')), float(request.GET.get('miu')), 
               int(request.GET.get('s')), int(request.GET.get('n')), request.GET.get('time'), cw, cs)
    elif name_model == 'MMSK':
        return m.Model(name_model, float(request.GET.get('l')), float(request.GET.get('miu')), 
               int(request.GET.get('s')), int(request.GET.get('k')), int(request.GET.get('n')),
               request.GET.get('time'), cw, cs)
    elif name_model == 'MG1':
        return m.Model(name_model, float(request.GET.get('l')), 
               float(request.GET.get('miu')), float(request.GET.get('variance')), 
               int(request.GET.get('n')), request.GET.get('time'), cw, cs)
    elif name_model == 'ME1':
        return m.Model(name_model, float(request.GET.get('l')), 
               float(request.GET.get('miu')), float(request.GET.get('k')), 
               int(request.GET.get('n')), request.GET.get('time'), cw, cs)
    elif name_model == 'MD1':
        return m.Model(name_model, float(request.GET.get('l')), 
               float(request.GET.get('miu')), int(request.GET.get('n')), request.GET.get('time'), cw, cs)