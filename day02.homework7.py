import random
def Game(put):
    list = ['正面','反面']
    ram = random.choice(list)
    if ram == put:
        print("恭喜你，猜对啦")
    else:
        print("很遗憾，猜错啦")

def Start():
    put = input("请输入一个猜测值：")
    Game(put)

Start()