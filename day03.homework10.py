def Student():
    list = []
    i = 1
    while i <= 10:
        nums = float(input("Enter ten numbers:"))
        list.append(nums)
        i += 1
    print(list)

    sum_ = 0
    for i in list:
        sum_ += i
        average = sum_/len(list)
    print("The mean is",average)
    
    x = 0
    x += (nums - average)**2
    deviation = (x/(len(list)-1))**0.5
    print("The standard deviation is",deviation)
Student()
