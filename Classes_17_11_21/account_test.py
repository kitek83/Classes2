import bank_account

def main():
    bal = float(input('Enter your money balance: '))
    savings = bank_account.Bank(bal)
    
    dep = float(input('Ener how much money you want to deposit: '))
    savings.deposit(dep)
    #now we will use __str__def(self):
    print(savings)
    
    cash = float(input('Enter how much money you want to withdraw: '))
    savings.withdraw(cash)
    print(savings)
    
main()