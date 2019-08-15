# import calendar 
# def num(year,month):
#     print(calendar.monthrange(year, month)[1])
# def start():
#     year = int(input('Enter year: ')) 
#     month = int(input('Enter month number: '))
#     num(year,month)
# start()

def Day(year,month): 
    day = -1
    if month >= 1 and month <= 12: 
        if month in (1,3,5,7,8,10,12): 
            day = 31
        elif month in (4,6,9,11):  
            day = 30
        else:
            if year % 400 == 0 :
                day = 29
            else:
                day = 28
        print("%d 年 %d 月 有 %d 天" % (year, month, day))
    else:
        print("月份输入有误！")
def Start ():
    year = int(input("Enter year: ")) 
    month = int(input("Enter month number: "))
    Day(year,month)
Start()

