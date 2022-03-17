#try tu ise function  def __str__(self):
class Bank:
    def __init__(self,bal):
        self.balance = bal

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insificient funds!')

    def get_balance(self):
        return self.balance

    def __str__(self):
        return 'Obecnie masz na koncie: ' + format(self.balance,'.2f')