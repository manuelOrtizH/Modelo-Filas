import math
from math import factorial

class MMSK(object):
    #λe tasa efectiva de arrivo = λ(1-Pn)
    def __init__(self,l,miu,s,k,n, time, cw, cs):
        #Constructor para inicializar todos los atributos
        self.n=n
        self.k=k 
        self.l = l #λ
        self.s = s #s
        self.cw = cw
        self.cs = cs
        self.time = time
        self.miu = miu #µ time = 20 minutos
        self.po=self.calculatePo()
        #poPer no es un atributo
        self.poPer = round(self.po * 100,3)
        self.le=self.calculateLe()
        self.p = self.calculateP()
        #pPer no es un atributo
        self.pPer = round(self.p * 100, 3)
        self.lq = self.calculateLQ()
        self.wq=self.calculateWq()
        self.w=self.calculateW()
        self.L=self.calculateL()
        self.pn=self.calculatePn(n)
        self.cn=self.calculateCn(n)
        self.ct = self.calculateTotalCost()
        self.variance = 0
    
    def calculateP(self):
        return round(self.l/(self.miu*self.s),3)        

    def calculatePo(self):
        sum1=0
        sum2=0
        for n in range(self.s+1):
            sum1+= (math.pow(self.l/self.miu, n))/factorial(n)        
        for n in range(self.s ,self.k):
            sum2+= (math.pow(self.l/(self.miu * self.s), (n+1) - self.s))
        sum2*=(math.pow(self.l/self.miu, self.s))/factorial(self.s)
        result = sum1 + sum2
        return round(1/result,4)
    
    def getPn(self,n):
        if(n<self.s): return (math.pow(self.l/self.miu,n)/factorial(n))*self.po
        elif(n>=self.s and n<=self.k): return ((math.pow((self.l/self.miu),n))/(factorial(self.s)*math.pow(self.s,(n)-self.s)))*self.po
        elif(n>self.k): return 0

    def calculatePn(self,n):
        return [round(self.getPn(i+1),6) for i in range(n)]

    def getCn(self,n):
        if(n<self.s): return math.pow(self.l/self.miu,n)/factorial(n)
        elif(n>=self.s and n <= self.k): return math.pow(self.l/self.miu,n)/(factorial(self.s)*math.pow(self.s,(n)-self.s))
        elif(n>self.k): return 0

    def calculateCn(self,n):
        return [round(self.getCn(i+1),6) for i in range(n)]
    
    def calculateLQ(self):
        return round((self.po*((math.pow(self.l/self.miu,self.s)*self.p)/(factorial(self.s)*(math.pow(1-self.p,2)))))*(1-math.pow(self.p,self.k-self.s)-(self.k-self.s)*math.pow(self.p,self.k-self.s)*(1-self.p)),3)
    
    def calculateL(self):
        return round(self.le*self.w,3)
    
    def calculateLe(self):
        return round(self.l*(1- self.getPn(self.k)),3)

    def calculateWq(self):
        return round(self.lq/self.le,3)
    
    def calculateW(self):
        return round(self.wq+(1/self.miu),3)

    def calculateTotalCost(self):
        return round(self.lq*self.cw+self.s*self.cs, 3)

    def __str__(self):
        #Imprimir todo los atributos
        return f'λ: {self.l}, µ: {self.miu}, p: {self.p}, p0: {self.po}, Pn: {self.pn}, Cn: {self.cn}, lq: {self.lq}, L: {self.L}, Wq: {self.wq}, W: {self.w}, λe: {self.le}'
   
# m = MMSK(2, 3, 3, 1,3)
# print(m)


