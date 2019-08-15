def Perimeter(a,b,c):
    if a + b > c and a + c > b and b + c > a :
         perimeter = a + b + c
         print("The perimeter is ",perimeter)
    else:
        print("输入的边长不合法")

def Start():
    a,b,c = eval(input("Enter three edges:"))
    Perimeter(a,b,c)

Start()