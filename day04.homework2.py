def sumDigits(n):
    sum = 0
    m = str(n)
    for i in range(len(m)):
        num = n//10**i%10
        sum += num
    print(sum) 

if __name__ == '__main__':
    n = int(input("请输入一个数字："))
    sumDigits(n) 
    