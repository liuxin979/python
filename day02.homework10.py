import random
def Game():
    size = ['Ace',2,3,4,5,6,7,8,9,10,'Jcke','Queen','King']
    color = ['blossom','hearts','diamonds','spade']
    size1 = random.choice(size)
    color1 = random.choice(color)
    print("The card you picked is the",size1,"of",color1)

Game()