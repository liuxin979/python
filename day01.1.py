import random
email = '14784743866@163.com'
password = 'lx19970912'
email1 = input("请输入邮箱账号：")
if '@163.com' not in email1:
    print("输入的账号不合法")
else:
    x = 0
    for i in range(4):
        password1 = input("请输入密码：")
        if email1 == email and password1 == password:
            print("登录成功")
            break
        elif x == 0 and password1 !=password:
            print("账号或者密码错误")
            count = 0
            for i in range(10):
                yzm = random.randint(1000,9999)
                print(yzm)
                num = eval(input("请输入验证码："))
                if num ==yzm:
                    print("验证码输入成功")
                    break
                elif num != yzm:
                    print("验证码不正确")
                    count +=1
                    num = eval(input("请重新输入验证码："))       
    else:
        print("账号已锁定")
        x +=1
