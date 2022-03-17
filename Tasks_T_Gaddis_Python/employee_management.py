#in program data is not save; save function is not working? why?
import employee
import pickle

SEARCH = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def main():
    employes = load_employees()
    #save(employes)
    choice = 0

#Wyszukanie pracownika w słowniku
    while choice != QUIT:
        choice = get_menu()
        if choice == SEARCH:
            search(employes)
        elif choice == ADD:
            add_employee(employes)
        elif choice == CHANGE:
            change_empl(employes)
        elif choice == DELETE:
            delete(employes)
        save(employes)

def load_employees():
   try:
       input_file = open('Employee.dat','ab')
       employees = pickle.load(input_file)
       input_file.close()
   except IOError:
       employee1 = employee.Employee('Sara Majewska', 47899, 'Księgowość', 'Zastępca dyrektora')
       employee2 = employee.Employee('Marek Jankowski', 39119, 'IT', 'Programista')
       employee3 = employee.Employee('Jan Kowalski', 81774, 'Produkcja', 'Inżynier')

       employees = {}
       employees[47899] = employee1
       employees[39119] = employee2
       employees[81774] = employee3
   print(employees)
   print()
   return employees
   

def get_menu():
    print('Menu:')
    print('--------------------------')
    print('1.Search for the employee.')
    print('2.Add new employee.')
    print('3.Change data for the existing employee.')
    print('4.Delete employee.')
    print('5.Quit the program.')
    print()
    choice = int(input('Enter number or 5 to quit:'))
    if choice < SEARCH or choice > QUIT:
        print('Enter correct number 1-5.')
    return choice

def search(employes):
    #search employe using identity_nr
    identity = int(input('Enter identity nr of the worker you are looking for: '))
    for key,val in employes.items():
        if identity == key:
            print(f'{val.get_name(),val.get_identity_nr(),val.get_department(),val.get_position()}')


def add_employee(employes):
    name = input('Enter name and surname: ')
    identity = int(input('Enter identity nr: '))
    dep = input('Enter department: ')
    pos = input('Enter position:')
    entry = employee.Employee(name,identity,dep,pos)


    employes[identity] = entry
    print('Osoba została dodana.')
    save(employes)

def change_empl(employes):
    identity = int(input('Enter identity nr:'))
    if identity in employes:
        name = input('Enter name and surname:')
        dep = input('Enter department: ')
        pos = input('Enter position: ')

        entry = employee.Employee(name,identity,dep,pos)
        employes[identity] = entry
        print('Data was updated.')
    else:
        print('Nr was not found.')

def delete(employes):
    empl_del = int(input('Enter identity nr to delete: '))
    if empl_del in employes:
        del employes[empl_del]
        print('Osoba została skasowana.')
    else:
        print('Nr nie został znaleziony.')

def save(employes):
    file_save = open('Employee.dat',mode='ab')
    pickle.dump(employes,file_save)
    file_save.close()


main()



















