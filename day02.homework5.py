def Package(weight1,price1,weight2,price2):
    value1 = price1 / weight1
    value2 = price2 / weight2
    if value1 > value2:
        print("Package 2 has the better price")
    else:
        print("Package 1 has the better price")

def Start():
    weight1,price1 = eval(input("Enter weight and price for package1:"))
    weight2,price2 = eval(input("Enter weight and price for package1:"))
    Package(weight1,price1,weight2,price2)

Start()