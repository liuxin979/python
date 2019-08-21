class LinearEquation(object):
    
    def __init__(self):
        pass
    
    def main(self):
        x1,y1=eval(input('请输入第一条直线的一个端点'))
        x2,y2=eval(input('请输入第一条直线的二个端点'))
        x3,y3=eval(input('请输入第二条直线的一个端点'))
        x4,y4=eval(input('请输入第二条直线的二个端点'))
        
        self.jishuan(x1,y1,x2,y2,x3,y3,x4,y4)
    
    def jishuan(self,x1,y1,x2,y2,x3,y3,x4,y4):
        a = y2-y1
        b = x2*y1-x1*y2
        c = x2-x1
        d = y4-y3
        e = x4*y3-x3*y4
        f = x4-x3
        
        self.gongshi(a,b,c,d,e,f)
    
    def gongshi(self,a,b,c,d,e,f):
        y = float(a*e-b*d)/(a*f-c*d)
        x = float(y*c-b)/a
        print('交点的坐标为：',(x,y))

if __name__ == "__main__":
    linearequation = LinearEquation()
    linearequation.main()
