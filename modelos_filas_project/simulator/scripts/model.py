from .mm1 import MM1
from .mms import MMS
from .mg1 import MG1
from .mmsk import MMSK
#Ignorar este archivo, se usará después
class Model:
    def __init__(self, name_model, *args):
        self.model = {'MM1': getMM1(args),
           'MMS': getMMS(args),
           'MG1': getMMS(args),
           'MMSK': getMMS(args)}.get(name_model, 'Ningún método seleccionado')
    
    def getMM1(self, args):
        return MM1(args[0], args[1], args[2])
    
    def getMMS(self, args):
        return MMS(args[0])
    
    def getMMSK(self, args):
        return MMSK(args[0])
    
    def getMG1(self, args):
        return MG1(args[0])



        
        
    