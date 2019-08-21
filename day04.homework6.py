def numberOfDaysInAYear(year):
    print("Years","\t","Days")
    for year in range(2010,2021):
        if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
            print(year,"\t",366) 
        else:
            print(year,"\t",365)

if __name__ == '__main__':
    year = 0
    numberOfDaysInAYear(year)
