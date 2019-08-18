def Statistics():
    integer_sum = 0
    positive_numbers = 0
    minus_numbers = 0
    temp = 1
    while temp == 1:
        integer = int(input("Enter an integer,the input ends if it is 0:"))
        if integer > 0 :
            positive_numbers += 1
        elif integer < 0:
            minus_numbers += 1
        else:
            break
    
        integer_sum += integer
    
    print(float(integer_sum / (positive_numbers + minus_numbers)))
    print(positive_numbers)
    print(minus_numbers)

Statistics()