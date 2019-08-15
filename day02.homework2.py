import random
def Game(c):
    a = random.randint(0,100)
    b = random.randint(0,100)       
    if c == a + b:
        print("答对了")
    else:
        print("答错了")    
def Start():
    c = int (input("请输入两个数字的和："))
    Game(c)
 
Start()