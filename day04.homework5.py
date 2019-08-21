def printChars(ch1,ch2,numberPerLine):
    count = 0
    for i in range (ch1,ch2):
        numberPerLine = chr(i)
        count +=1
        print(numberPerLine,end = " ")
        if count % 10 ==0:
            print("\n")

if __name__ == '__main__':
    ch1 = 73
    ch2 = 91
    numberPerLine = ""
    printChars(ch1,ch2,numberPerLine)
