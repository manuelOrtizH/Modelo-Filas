import math
from math import factorial

class MMS(object):
    def __init__(self,l,time,n,s):
        #Constructor para inicializar todos los atributos
        self.l = l #λ
        self.s = s #s
        self.miu = (1/time)*60 #µ time = 20 minutos
        self.p = self.calculateP()
        self.po=self.calculatePo()
        self.lq = self.calculateLQ()
        self.L=self.calculateL()
        self.pn=self.calculatePn(n)
        self.cn=self.calculateCn(n)
        self.wq=self.calculateWq()
        self.w=self.calculateW()
    
    def calculateP(self):
        return round(self.l/(self.miu*self.s),3)

    def calculatePo(self):
        sum=0
        for n in range(0,self.s):
            sum=sum+((math.pow((self.l/self.miu),n)/(factorial(n)))+((math.pow(self.l/self.miu,self.s)/(factorial(self.s)))*(1/(1-(self.l/self.s*self.miu)))))
        return round(1/sum,3)
    
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
        return round(self.po*((math.pow(self.l/self.miu,self.s)*self.p)/(factorial(self.s)*(math.pow(1-self.p,2)))),3)
    
    def calculateL(self):
        return round(self.lq+(self.l/self.miu),3)

    def calculateWq(self):
        return round(self.lq/self.l,3)
    
    def calculateW(self):
        return round(self.wq+(1/self.miu),3)

    def __str__(self):
        #Imprimir todo los atributos
        return f'λ: {self.l}, µ: {self.miu}, p: {self.p}, p0: {self.po}, Pn: {self.pn}, Cn: {self.cn}, lq: {self.lq}, L: {self.L}, Wq: {self.wq}, W: {self.w}'
   
m = MMS(60, 20, 4, 3)
print(m)


