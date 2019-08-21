class Rectangle(object):
    def __init__(self,width = 1,height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width  +self.height) * 2

    def test(self):
        r1 = Rectangle(4,40)
        print('r1的宽是>>',r1.width)
        print('r1的高是>>',r1.height)
        print('r1的面积是>>',r1.getArea())
        print('r1的周长是>>',r1.getPerimeter())
        r2 = Rectangle(3.5,35.7)
        print('r2的宽是>>',r2.width)
        print('r2的高是>>',r2.height)
        print('r2的面积是>>',r2.getArea())
        print('r2的周长是>>',r2.getPerimeter())

if __name__ == "__main__":
    x = Rectangle()
    x.test()
