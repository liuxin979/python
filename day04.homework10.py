import random
def suiji():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    num3 = num1 + num2
    if num3 == 2 or num3 == 3 or num3 == 12:
        print("你输了")
    elif num3 == 7 or num3 == 11:
        print("你赢了")
    else:
        for i in range(1,1000):
            num4 = random.randint(1,6)
            num5 = random.randint(1,6)
            num6 = num5 + num4
            if num6 == 7:
                print("你输了")
                break
            elif num6 == num3:
                print("你赢了")

if __name__ == "__main__":
    suiji()