class BankAccount:
    def __init__(self,bal):
        self.balance = bal

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Nie masz wystarczajcych srodkow!')

    def get_balance(self):
        return self.balance

    #metoda informujaca o biezacym stanie obiektu
    def __str__(self):
        return 'Wysokosc salda wynosi ' + format(self.balance,'.2f')