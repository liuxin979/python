def Minnum():
    n = 0
    while n ** 2 < 12000:
        n += 1
    print(n)
def Maxnum():
    n1 = 0
    while n1 ** 3 < 12000:
        n1 += 1
    print(n1-1)

def Start():
    Minnum()
    Maxnum()

Start()