def displaySortedNumber(num1,num2,num3):
    list = [num1,num2,num3]
    list_ = sorted(list)
    print("The sorted numbers are:",list_)

if __name__ == '__main__':
    num1,num2,num3 = eval(input("Enter three numbers："))
    displaySortedNumber(num1,num2,num3)