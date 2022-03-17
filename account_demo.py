import accounts

def main():
    print('Podaj dane dotyczące konta oszczędnościowego: ')
    acc_num = int(input('Podaj nr konta: '))
    int_rate = float(input('Podaj oprocentowanie: '))
    bal = float(input('Saldo: '))

    savings = accounts.SavingAccount(acc_num,int_rate,bal)

    print('Podaj dane dotyczące certyfikatu depozytowego: ')
    acc_num = int(input('Nr konta: '))
    int_rate = float(input('Oprocentowanie: '))
    bal = float(input('Saldo: '))
    mat_date = input('Data wykupu:')

    cd = accounts.CD(acc_num,int_rate,bal,mat_date)

    print('O to wprowadzone dane: ')
    print('Konto oszczędnościowe: ')
    print(f'Nr konta: {savings.get_account_num()}')
    print(f'Oprocentowanie: {savings.get_interest_rate()}')
    print(f'Saldo: {savings.get_balance()}')
    print()
    print('------------------------------')
    print('CD:')
    print(f'Nr konta: {cd.get_account_num()}')
    print(f'Oprocentowanie: {cd.get_interest_rate()}')
    print(f'Saldo: {cd.get_balance()}')
    print(f'Data wykupu: {cd.get_maturity_date()}')


main()