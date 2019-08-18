def Tuition():
    dorlla = 10000
    for i in range(14):
        dorlla = dorlla * 0.05 + dorlla
        if i == 11:
            print(dorlla)
    print(dorlla)

Tuition()