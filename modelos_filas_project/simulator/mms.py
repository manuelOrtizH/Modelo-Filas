import math
from math import factorial
from fractions import Fraction

class MMS(object):
    def __init__(self,l,miu,s,n, time):
        #Constructor para inicializar todos los atributos
        self.l = l #λ
        self.s = s #s
        self.n = n
        self.time = time
        self.miu = miu #µ time = 20 minutos
        self.p = self.calculateP()
        self.pPer = round(self.p * 100, 3)
        self.po=self.calculatePo()
        self.poPer = round(self.po * 100,3)
        self.lq = self.calculateLQ()
        self.L=self.calculateL()
        self.pn=self.calculatePn(n)[n-1]
        self.pnPer = round(self.pn*100,3)
        self.cn=self.calculateCn(n)[n-1]
        self.cnPer = round(self.cn * 100, 3)
        self.wq=self.calculateWq()
        self.w=self.calculateW()
    
    def calculateP(self):
        return round(self.l/(self.miu*self.s),3)

    def calculatePo(self):
        s = 0
        for n in range(self.s):
            s += ( math.pow((self.l/self.miu), n)/ factorial(n) )
        s += (( math.pow((self.l/self.miu), self.s)/ factorial(self.s) )) * (1/(1-(self.l/(self.s*self.miu))))   
        return round(1/s,3)
    
    def getPn(self,i):
        if(i+1<self.s):
            pn = (math.pow(self.l/self.miu,i+1)/factorial(i+1))*self.po
        elif(i+1>=self.s):
            pn = ((math.pow((self.l/self.miu),i+1))/(factorial(self.s)*math.pow(self.s,(i+1)-self.s)))*self.po
        return pn

    def calculatePn(self,n):
        return [round(self.getPn(i),3) for i in range(n)]

    def getCn(self,i):
        if(i+1<self.s):
            cn = math.pow(self.l/self.miu,i+1)/factorial(i+1)
        elif(i+1>=self.s):
            cn = math.pow(self.l/self.miu,i+1)/(factorial(self.s)*math.pow(self.s,(i+1)-self.s))
        return cn

    def calculateCn(self,n):
        return [round(self.getCn(i),3) for i in range(n)]
    
    def calculateLQ(self):
        return round(((math.pow(self.l/self.miu, 2)*self.p)/(factorial(self.s)*(math.pow(1-self.p,2)))),3)
    
    def calculateL(self):
        return round(self.lq+(self.l/self.miu),3)

    def calculateWq(self):
        return round(self.lq/self.l,3)
    
    def calculateW(self):
        return round(self.wq+(1/self.miu),3)

    def __str__(self):
        #Imprimir todo los atributos
        return f'λ: {self.l}, µ: {self.miu}, p: {self.p}, p0: {self.po}, Pn: {self.pn}, Cn: {self.cn}, lq: {self.lq}, L: {self.L}, Wq: {self.wq}, W: {self.w}'
   
# m = MMS(100, 60, 0, 2)
# print(m)


