import math
class MG1(object):
    def __init__(self, l, time, n):
        #Constructor para inicializar todos los atributos
        self.l = l
        self.po = calculatePo()
        self.pn = calculatePn(n)
        self.miu = (1/time)*60
        self.variance = math.pow(1/(self.miu*self.miu),2)
        self.p = calculateP()
        self.lq = calculateLq()
        self.wq = calculateWq()
        self.w = calculateW()
        self.L = calculateL()

    def calculatePn(self, n):
        return [math.pow(self.p, i+1) * self.po for i in range(n)]

    def calculatePo(self):
        return 1 - self.p

    def calculateLq(self):
        return (((self.l * self.l) * self.variance + (self.p * self.p)) / (2*(1-self.p)) )

    def calculateWq(self):
        return self.lq/self.l

    def calculateW(self):
        return self.wq + (1/self.miu)

    def calculateP(self):
        return self.l/self.miu

    def calculateL(self):
        return self.l * self.w

    def __str__(self):
        return f'n: {self.n}, '
        #Imprimir todo los atributos

m = MG1(9, 5, 1)