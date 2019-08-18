def Add():
    a = 0
    for i in range(1,98,2):
        a += i/(i+2)
    print(a)

Add()