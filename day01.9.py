num = eval(input("Enter a number between 0 and 1000:"))
bai = num // 100 % 10
shi = num // 10 % 10
ge = num // 1 % 10
arr = [bai,shi,ge]
sum1 = sum(arr)
print("The sum of digits is：%d" % (sum1))