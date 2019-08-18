def Num():
    count = 0
    for i in range (100,1001):
        if i % 5 == 0 and i % 6 == 0:
            count +=1
            print(i,end = ' ')
            if count % 10 == 0:   
                print('\n')
Num()