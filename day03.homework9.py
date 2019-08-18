def Num():
    list = []
    for i in range(1,8,):
        for j in range(1,8):
            if i != j and sorted([i,j]) not in list:
                list.append([i,j])
    print(list)
    print("The total number of all combinations is",len(list))

Num()