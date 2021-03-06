import math

class MM1(object):
    #lambda = tasa media de llegadas
    #miu (碌) = tasa media de servicios
    #p (饾湆) = factor de utilizaci贸n de la instalaci贸n del servicio
    #lq es algo
    def __init__(self, l, miu, n, time, cw, cs):
        #Constructor para inicializar todos los atributos
        self.l = l #位
        self.miu = miu #位碌 time = 20 minutos
        self.s = 1
        self.n = n
        self.time = time
        self.cw = cw
        self.cs = cs
        self.p = self.calculateP() #饾湆 
        #pPer no es un atributo
        self.pPer = round(self.p * 100, 3)
        self.po = self.calculatePo()
        self.poPer = round(self.po * 100,3)
        self.cn = self.calculateCn(n)
        #cnPer no es un atributo
        #self.cnPer = round(self.cn * 100, 3)
        self.pn = self.calculatePn(n)
        #pnPer no es un atributo
        #self.pnPer = round(self.pn * 100, 3)
        self.lq = self.calculateLQ()
        self.L = self.calculateL()
        self.wq = self.calculateWq()
        self.w = self.calculateW()
        self.ct = self.calculateTotalCost()
        self.k = 0
        self.variance = 0
        
    def calculateP(self):
        return round(self.l/self.miu,3)

    def calculatePo(self):
        return round(1-self.p, 3)

    def calculateCn(self, n):
        return [round(math.pow(self.p, x+1),6) for x in range(n)]

    def calculatePn(self, n):
        return [round(math.pow(self.p, x+1)* self.po,6) for x in range(n)]

    def calculateLQ(self):
        return round((self.l*self.l)/(self.miu*(self.miu-self.l)),3)

    def calculateL(self):
        return round(self.l/(self.miu - self.l),3)
    
    def calculateWq(self):
        return round(self.l/(self.miu * (self.miu - self.l)),3)

    def calculateW(self):
        return round(1/(self.miu - self.l) , 3)

    def calculateTotalCost(self):
        return round(self.lq*self.cw+self.s*self.cs, 3)

    def __str__(self):
        #Imprimir todo los atributos
        return f'位: {self.l}, 碌: {self.miu}, 饾湆: {self.p}, P0: {self.po}, pn: {self.pn}, Cn: {self.cn},lq: {self.lq}, L: {self.L}, Wq: {self.wq}, W: {self.w}'
        
   
# m = MM1(2, 20, 4)
# print(m)