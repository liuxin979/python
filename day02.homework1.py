def Algebra(a,b,c): 
    r1 = (-b + ((b **2 - 4 * a * c) ** 0.5)) / (2 * a)
    r2 = (-b - ((b **2 - 4 * a * c) ** 0.5)) / (2 * a)
    discriminant = (b **2 - 4 * a * c)
    if discriminant > 0 :
        print("The roots are",r1,"are",r2)
    elif discriminant == 0:
        print("The root is ",r1)
    else:
        print("The equation has no real roots")

def Start():
    a, b, c = eval(input("Enter a,b,c:"))
    Algebra(a,b,c)

Start()