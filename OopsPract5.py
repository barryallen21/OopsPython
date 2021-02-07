class bank_ac():

    def get(self):
        self.acc_no = int(input("enter account no:"))
        self.acc_type = input("enter account type:")
        self.balance = 5000

class deposit(bank_ac):

    def dep(self):
        self.d = int(input("enter amount to deposit:"))
        self.balance = self.balance+ self.d
        print("the current balance:",self.balance)

class withdrawal(deposit):

    def withd(self):
        wi = int(input("enter amount to withdraw:"))
        self.balance = self.balance - wi
        if(self.balance > 500):
            print("remaining balance:",self.balance)

        else:
            print("cannot withdraw")

ob1 = withdrawal()
ob1.get()
ob1.dep()
ob1.withd()
