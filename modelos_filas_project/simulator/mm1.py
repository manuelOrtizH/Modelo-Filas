import math

class MM1(object):
    #lambda = tasa media de llegadas
    #miu (µ) = tasa media de servicios
    #p (𝜌) = factor de utilización de la instalación del servicio
    #lq es algo
    def __init__(self, l, miu, n):
        #Constructor para inicializar todos los atributos
        self.l = l #λ
        self.miu = miu #µ time = 20 minutos
        self.p = self.calculateP() #𝜌 
        self.po = self.calculatePo()
        self.cn = self.calculateCn(n)
        self.pn = self.calculatePn(n)
        self.lq = self.calculateLQ()
        self.L = self.calculateL()
        self.wq = self.calculateWq()
        self.w = self.calculateW()
        
    def calculateP(self):
        return round(self.l/self.miu,3)

    def calculatePo(self):
        return round(1-self.p, 3)

    def calculateCn(self, n):
        return [round(math.pow(self.p, i+1),3) for i in range(n)]

    def calculatePn(self, n):
        return [round(math.pow(self.p, i+1)* self.po,3) for i in range(n)]

    def calculateLQ(self):
        return round((self.l*self.l)/(self.miu*(self.miu-self.l)),3)

    def calculateL(self):
        return round(self.l/(self.miu - self.l),3)
    
    def calculateWq(self):
        return round(self.l/(self.miu * (self.miu - self.l)),3)

    def calculateW(self):
        return round(1/(self.miu - self.l) , 3)

    def __str__(self):
        #Imprimir todo los atributos
        return f'λ: {self.l}, µ: {self.miu}, 𝜌: {self.p}, P0: {self.po}, pn: {self.pn}, Cn: {self.cn},lq: {self.lq}, L: {self.L}, Wq: {self.wq}, W: {self.w}'
        
   
# m = MM1(2, 20, 4)
# print(m)