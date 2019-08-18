def Pi():
    pi = 0 
    for i in range(1,100000):
        pi += 4*((-1)**(i+1)/(2*i-1))       
    print(pi)
Pi()