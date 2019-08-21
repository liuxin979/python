class LinearEquation(object):
    def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self._e = e
        self._f = f
    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    @property
    def c(self):
        return self._c
    @property
    def d(self):
        return self._d
    @property
    def e(self):
        return self._e
    @property
    def f(self):
        return self._f    
        
    def getx(self):
        x = (self._e * self._d - self._b * self._f) / (self._a * self._d - self._b * self._c)
        return x
    def gety(self):
        y = (self._a * self._f - self._e * self._c) / (self._a * self._d - self._b * self._c)        
        return y
    def isSolvable(self,a,b,c,d):
        if self._a * self._d - self._b * self._c != 0:
            print(True)
    
if __name__ =="__main__":
    num = LinearEquation(1,2,3,4,5,6)
    print(num.getx())
    print(num.gety())