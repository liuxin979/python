def Add():
    a = 0
    for i in range(50000,0,-1):
        a += 1/i
    print(a)

Add()