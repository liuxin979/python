import math
radius,length = eval(input("Enter the radius and length of a cylinder:"))
area = radius * radius * math.pi
volum = area * length
print("The area is：%.2f" % (area))
print("The voume is：%.2f" % (volum))