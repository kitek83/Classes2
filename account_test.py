import bankaccount
def main():
   start_bal = float(input('Podaj poczatkowa wysokosc salda: '))
   #utworzenie obiektu
   savings = bankaccount.BankAccount(start_bal)
   print('Obecnie masz na koncie: ',savings.get_balance())

   pay = float(input('Podaj kwote, ktora zarobiles w tym miesiacu: '))
   savings.deposit(pay)

   print()
   print(f'Twoja zarobiona kwota {format(pay,".2f")} zpstala dodana do salda.')
   print(f'Twoje saldo wynosi {format(savings.get_balance(),".2f")}.')

   cash = float(input('Podaj jaka kwote chcialbys wyplacic: '))
   savings.withdraw(cash)
   print()
   print(f'Twoje obecne saldo po wyplaceniu {cash} wynosi: {format(savings.get_balance(),".2f")}.')




main()