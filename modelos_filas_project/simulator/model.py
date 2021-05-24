from simulator import mm1,mms,mmsk,mg1
#Ignorar este archivo, se usará después
class Model:
    def __init__(self, name_model, *args):
        if name_model == 'MM1':
            self.model = mm1.MM1(args[0], args[1], args[2], args[3])
        elif name_model == 'MMS':
            self.model = mms.MMS(args[0],args[1],args[2],args[3], args[4])
        elif name_model == 'MMSK':
            self.model = mmsk.MMSK(args[0], args[1], args[2], args[3], args[4], args[5])
        elif name_model == 'MG1':
            self.model = mg1.MG1(args[0], args[1], args[2], args[3], args[4])

    def totalCost(self, cw, cs):
        return round(self.model.lq*cw+self.model.s*cs, 3)

# m_mm1 = Model('MM1', 2, 3, 4)
# print('MM1: ')
# print(m_mm1.model, '\n')
# m_mms = Model('MMS', 100, 60, 0, 2)
# print('MMS: ')
# print(m_mms.model, '\n')
# m_mmsk = Model('MMSK', 2, 3, 3, 1,3)
# print('MMSK:')
# print(m_mmsk.model, '\n')
# print(m_mmsk.totalCost(20,10) ,'USD ')
        

    