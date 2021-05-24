import math
class MG1(object):
    def __init__(self, l, miu, variance ,n, time):
        #Constructor para inicializar todos los atributos
        self.l = l
        self.n = n
        self.miu = miu
        self.s = 1
        self.variance = variance
        self.time = time
        self.p = self.calculateP()
        self.pPer = round(self.p * 100, 3)
        self.po = self.calculatePo()
        self.poPer = round(self.po * 100,3)
        self.pn = self.calculatePn(n)
        self.pnPer = round(self.pn * 100,3)
        self.lq = self.calculateLq()
        self.wq = self.calculateWq()
        self.w = self.calculateW()
        self.L = self.calculateL()

    def calculateP(self):
        return self.l/self.miu

    def calculatePo(self):
        return 1 - self.p

    def calculatePn(self, n):
        return round(math.pow(self.p, n) * self.po,3)

    def calculateLq(self):
        return (((self.l * self.l) * (self.variance*self.variance) + (self.p * self.p)) / (2*(1-self.p)) )

    def calculateWq(self):
        return self.lq/self.l

    def calculateW(self):
        return self.wq + (1/self.miu)

    def calculateL(self):
        return self.l * self.w

    def __str__(self):
        return f'lq: {self.lq}, L: {self.L}, w: {self.w}, wq: {self.wq}, Po: {self.po}, p: {self.p}'
        #Imprimir todo los atributos

# m = MG1(0.05, 0.066, 1)
# print(m)