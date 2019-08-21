def sushu():
    i = 2
    c = []
    d = []
    while i <=31:
        j = 2
        while j <= i:
            if i % j ==0:
                if i == j:
                    c.append(i)
                break
            j += 1
        i += 1
    print(c) 
    for x in c:
        sushu = 2 ** x - 1
        d.append(sushu)
    print(d) 


    
          
if __name__ == '__main__':
    sushu()