def Shengxu(a,b,c):
    list = [a,b,c]
    list.sort()
    print(list)

def Start():
    a,b,c = eval(input("请输入三个整数："))
    Shengxu(a,b,c)

Start()