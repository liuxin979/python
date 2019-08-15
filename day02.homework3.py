def Day(day):  
    if day == 0:
        print('星期日')
    elif day == 1:
        print('星期一')
    elif day == 2:
        print('星期二')
    elif day == 3:
        print('星期三')
    elif day == 4:
        print('星期四')
    elif day == 5:
        print('星期五')
    elif day == 6:
        print('星期六')
        
def Futureday(day,futureday):
    day2 = day + futureday
    if day2 >= 7:
        day3 = (day2) % 7
        Day(day3)
    else:
        Day(day2)
    
def Start():
    day = eval(input("Enter today's day:"))
    futureday = eval(input("Enter the number of days elapsed since today:"))
    Day(day)
    Futureday(day,futureday)

Start()


