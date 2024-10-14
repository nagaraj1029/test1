class Account:
    def __init__(self,balance,accno):
        self.balance = balance
        self.accno = accno
    
    def debit(self,amount):
        self.balance -=amount
        print("Rs :",amount,"debited")
        print("total balance after debit:",self.get_balance())

    def credit(self,amount):
        self.balance +=amount
        print("Rs :",amount,"Credited")
        print("total balance after credit:",self.get_balance())
    
    def get_balance(self):
        return self.balance
    

acc1 = Account(100000,101)
acc1.debit(1000)
acc1.credit(25000)
acc1.debit(9000)

