import employee

def main():
    employee1 = employee.Employee('Sara Majewska',47899,'Księgowość','Zastępca dyrektora')
    employee2 = employee.Employee('Marek Jankowski',39119,'IT','Programista')
    employee3 = employee.Employee('Jan Kowalski',81774,'Produkcja','Inżynier')
    
    employees = [employee1,employee2,employee3]
    
    for employe in employees:
        print('Dane pracownika: ')
        print('-----------------------')
        print(f'Imię i nazwisko: {employe.get_name()}')
        print(f'Nr identyfikacyjny: {employe.get_identity_nr()}')
        print(f'Dział: {employe.get_department()}')
        print(f'Stanowisko: {employe.get_position()}')
        print()

main()