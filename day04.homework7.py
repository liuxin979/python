def distance(x1,y1,x2,y2):
    dis = ((x1-x2)**2+(y1-y2)**2)**0.5
    print(dis)

if __name__ == '__main__':
    x1,y1 = eval(input("x1,y1："))
    x2,y2 = eval(input("x2,y2："))
    distance(x1,y1,x2,y2)