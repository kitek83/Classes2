import bankaccount2

start_bal = float(input('Podaj poczatkowa wyskosc salda: '))
#utworzenie obiektu
savings = bankaccount2.BankAccount(start_bal)

pay = float(input('Podaj swoj miesieczny zarobek: '))
savings.deposit(pay)
print(savings)
print()

cash = float(input('Podaj ilosc pieniedzy, ktora chcesz wyplacic: '))
savings.withdraw(cash)
print(savings)