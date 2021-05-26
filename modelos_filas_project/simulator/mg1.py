import math
class MG1(object):
    def __init__(self, l, miu, variance ,n, time, cw, cs):
        #Constructor para inicializar todos los atributos
        self.l = l
        self.n = n
        self.miu = miu
        self.s = 1
        self.cw = cw 
        self.cs = cs
        self.variance = variance
        self.time = time
        self.p = self.calculateP()
        #pPer no es atributo
        self.pPer = round(self.p * 100, 3)
        self.po = self.calculatePo()
        #poPer no es atributo
        self.poPer = round(self.po * 100,3)
        self.pn = self.calculatePn(n)
        self.lq = self.calculateLq()
        self.wq = self.calculateWq()
        self.w = self.calculateW()
        self.L = self.calculateL()
        self.ct = self.calculateTotalCost()

    def calculateP(self):
        return round(self.l/self.miu,3)

    def calculatePo(self):
        return round(1 - self.p,3)

    def calculatePn(self, n):
        return [round(math.pow(self.p, i+1) * self.po,6) for i in range(n)]

    def calculateLq(self):
        return round((((self.l * self.l) * (self.variance*self.variance) + (self.p * self.p)) / (2*(1-self.p)) ),3)

    def calculateWq(self):
        return round(self.lq/self.l,3)

    def calculateW(self):
        return round(self.wq + (1/self.miu),3)

    def calculateL(self):
        return round(self.l * self.w,3)

    
    def calculateTotalCost(self):
        return round(self.lq*self.cw+self.s*self.cs, 3)

    def __str__(self):
        return f'lq: {self.lq}, L: {self.L}, w: {self.w}, wq: {self.wq}, Po: {self.po}, p: {self.p}'
        #Imprimir todo los atributos

# m = MG1(0.05, 0.066, 1)
# print(m)