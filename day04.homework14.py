import math
class RegularPolygon(object):
    def __init__(self,n = 3,side = 1,x = 0,y = 0):
        self.n = n
        self.side = side
        self.x = x
        self.y = y

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, new_n):
        self._n = new_n

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, new_side):
        self._side = new_side

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    def getPerimeter(self):
        return self.n * self.side

    def getArea(self):
        return self.n * self.side ** 2 / (4 * math.tan(math.pi / self.n))

if __name__ == "__main__":
    r1 = RegularPolygon()
    print("周长为：",r1.getPerimeter())
    print("面积为：",r1.getArea())
    print("################################")
    r2 = RegularPolygon(6,4)
    print("周长为：",r2.getPerimeter())
    print("面积为：",r2.getArea())
    print("################################")
    r3 = RegularPolygon(10,4,5.6,7.8) 
    print("周长为：",r3.getPerimeter())
    print("面积为：",r3.getArea())   
