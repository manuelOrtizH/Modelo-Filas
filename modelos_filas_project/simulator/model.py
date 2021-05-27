from simulator import mm1,mms,mmsk,mg1,me1,md1
#Ignorar este archivo, se usará después
class Model:
    def __init__(self, name_model, *args):
        if name_model == 'MM1':
            self.model = mm1.MM1(args[0], args[1], args[2], args[3], args[4], args[5])
        elif name_model == 'MMS':
            self.model = mms.MMS(args[0],args[1],args[2],args[3], args[4], args[5], args[6])
        elif name_model == 'MMSK':
            self.model = mmsk.MMSK(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7])
        elif name_model == 'MG1':
            self.model = mg1.MG1(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        elif name_model == 'ME1':
            self.model = me1.ME1(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
        elif name_model == 'MD1':
            self.model = md1.MD1(args[0], args[1], args[2], args[3], args[4], args[5])