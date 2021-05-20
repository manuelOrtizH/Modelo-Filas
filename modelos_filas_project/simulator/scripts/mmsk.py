import math
from math import factorial

class MMSK(object):
    def __init__(self,l,time,n,s,k):
        #Constructor para inicializar todos los atributos
        self.n=n
        self.k=k 
        self.l = l #λ
        self.s = s #s
        self.miu = (1/time)*60 #µ time = 20 minutos
        self.po=self.calculatePo()
        self.le=self.calculateLe()
        self.p = self.calculateP()
        self.lq = self.calculateLQ()
        self.wq=self.calculateWq()
        self.w=self.calculateW()
        self.L=self.calculateL()
        self.pn=self.calculatePn(n)
        self.cn=self.calculateCn(n)
        


    def calculateP(self):
        return round(self.l/(self.miu*self.s),3)

    def calculatePo(self):
        sum=0
        sum2=0
        for n in range(0,self.s+1):
            sum=sum+(math.pow((self.l/self.miu),n)/(factorial(n)))+(math.pow(self.l/self.miu,self.s)/(factorial(self.s)))
        for n in range(self.s+1,self.k):
            sum2=sum2+math.pow(self.l/(self.s*self.miu),self.n-self.s)
        return round(1/sum*sum2,3)
    
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
        return round((self.po*((math.pow(self.l/self.miu,self.s)*self.p)/(factorial(self.s)*(math.pow(1-self.p,2)))))*(1-math.pow(self.p,self.k-self.s)-(self.k-self.s)*math.pow(self.p,self.k-self.s)*(1-self.p)),3)
    
    def calculateL(self):
        return round(self.le*self.w,3)
    
    def calculateLe(self):
        return self.l*(1-self.getPn(self.k))

    def calculateWq(self):
        return round(self.lq/self.le,3)
    
    def calculateW(self):
        return round(self.wq+(1/self.miu),3)

    def __str__(self):
        #Imprimir todo los atributos
        return f'λ: {self.l}, µ: {self.miu}, p: {self.p}, p0: {self.po}, Pn: {self.pn}, Cn: {self.cn}, lq: {self.lq}, L: {self.L}, Wq: {self.wq}, W: {self.w}, λe: {self.le}'
   
m = MMSK(60, 20, 4, 3,8)
print(m)


