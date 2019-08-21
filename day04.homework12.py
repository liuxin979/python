class Account(object):
    def __init__(self, id_=0, balance=100.0, annualInterestRate=0.0):
        self._id = id_
        self._balance = balance
        self._annualInterestRate = annualInterestRate

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        return self._balance

    @property
    def annualInterestRate(self):
        return self._annualInterestRate

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @annualInterestRate.setter
    def annuallInterestRate(self, new_annualInterestRate):
        self._annuallInterestRate = new_annualInterestRate

    def getMonthlyInterestRate(self):
        return self._annualInterestRate/12/100

    def getMonthlyInterest(self):
        rate = self.getMonthlyInterestRate()
        res = self._balance * rate
        return res

    def withdraw(self, money):
        if self._balance >= money:
            self._balance -= money
            print("您已成功取出：%.2f" % money)
            print("您的余额为：%.2f" % self._balance)
        else:
            print("您的余额不足")
            print("您的余额为：%.2f" % self._balance)
    
    def deposit(self, money):
        self._balance += money
        print("您已成功存入：%.2f" % money)
        print("您的余额为：%.2f" % self._balance)


if __name__ == "__main__":
    a = Account(id_=1122, balance=20000, annualInterestRate=4.5)
    a.withdraw(2500)
    a.deposit(3000)
    print("月利率为：",a.getMonthlyInterestRate())
    print("月利息为：",a.getMonthlyInterest())
