def futureInvestmenValue(investmentAmount,AnnualInterestRate):
    monthlyInterestRate = float(AnnualInterestRate)/12/100
    print("Years","\t","Future Value")
    for years in range(1,31):
        futureValue = investmentAmount * ((1 + monthlyInterestRate)**(12*years))
        print(years,"\t","%.2f"%futureValue)

if __name__ == '__main__':
    investmentAmount = eval(input("The amount invested："))
    AnnualInterestRate = eval(input("Annual interest rate："))
    futureInvestmenValue(investmentAmount,AnnualInterestRate)