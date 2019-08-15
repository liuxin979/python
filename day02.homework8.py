import random
def Game(U_res):
    C_res = random.randint(0,2)
    if C_res == U_res:
        print('平局')
    else:
        if C_res == 0 and U_res == 1:
            print('电脑赢了')
        elif C_res == 1 and U_res == 2:
            print('电脑赢了')
        elif C_res == 2 and U_res == 0:
            print('电脑赢了')
        else:
            print('你赢了')

def Start():
    U_res = int(input('scissor (0),rock (1),paper (2):'))
    Game(U_res)

Start()