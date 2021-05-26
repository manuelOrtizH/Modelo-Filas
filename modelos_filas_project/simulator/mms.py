import math
from math import factorial

class MMS(object):
    def __init__(self,l,miu,s,n, time, cw, cs):
        #Constructor para inicializar todos los atributos
        self.l = l #λ
        self.s = s #s
        self.n = n
        self.time = time
        self.cw = cw
        self.cs = cs
        self.miu = miu
        self.p = self.calculateP()
        #pPer no es un atributo
        self.pPer = round(self.p * 100, 3)
        self.po=self.calculatePo()
        #poPer no es un atributo
        self.poPer = round(self.po * 100,3)
        self.lq = self.calculateLQ()
        self.L=self.calculateL()
        self.pn=self.calculatePn(n)
        self.cn=self.calculateCn(n)
        self.wq=self.calculateWq()
        self.w=self.calculateW()
        self.ct = self.calculateTotalCost()
    
    def calculateP(self):
        return round(self.l/(self.miu*self.s),3)

    def calculatePo(self):
        s = 0
        for n in range(self.s):
            s += ( math.pow((self.l/self.miu), n)/ factorial(n) )
        s += (( math.pow((self.l/self.miu), self.s)/ factorial(self.s) )) * (1/(1-(self.l/(self.s*self.miu))))   
        return round(1/s,3)
    
    def getPn(self,n):
        if(n<=self.s): return (math.pow(self.l/self.miu,n)/factorial(n))*self.po
        elif(n>self.s): return ((math.pow((self.l/self.miu),n))/(factorial(self.s)*math.pow(self.s,(n)-self.s)))*self.po

    def calculatePn(self,n):
        return [round(self.getPn(i+1),6) for i in range(n)]

    def getCn(self,n):
        if(n<self.s): return math.pow(self.l/self.miu,n)/factorial(n)
        elif(n>=self.s): return math.pow(self.l/self.miu,n)/(factorial(self.s)*math.pow(self.s,(n)-self.s))
        
    def calculateCn(self,n):
        return [round(self.getCn(i+1),6) for i in range(n)]
    
    def calculateLQ(self):
        return round(((math.pow(self.l/self.miu, 2)*self.p)/(factorial(self.s)*(math.pow(1-self.p,2)))),3)
    
    def calculateL(self):
        return round(self.lq+(self.l/self.miu),3)

    def calculateWq(self):
        return round(self.lq/self.l,3)
    
    def calculateW(self):
        return round(self.wq+(1/self.miu),3)

    
    def calculateTotalCost(self):
        return round(self.lq*self.cw+self.s*self.cs, 3)

    def __str__(self):
        #Imprimir todo los atributos
        return f'λ: {self.l}, µ: {self.miu}, p: {self.p}, p0: {self.po}, Pn: {self.pn}, Cn: {self.cn}, lq: {self.lq}, L: {self.L}, Wq: {self.wq}, W: {self.w}'
   
# m = MMS(100, 60, 0, 2)
# print(m)


