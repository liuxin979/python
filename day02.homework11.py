def Decide (num):
    if num >=100 and num <=999:
        num = str(num)
        num2 = num[::-1]
        if num2 == num:
            print("是回文数")
        else:
            print("不是回文数")
    else:
        print("输入的数字不合法") 

def Start():
    num = int(input("请输入一个三位数："))
    Decide(num)
    
Start()