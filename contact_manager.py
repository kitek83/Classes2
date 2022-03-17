import pickle
import contacts

#Stale globalne obslugujace opcje menu
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():
    my_contacts = load_contacts()
    print(3*'-----------------')
    for key, val in my_contacts.items():
        print(f'{key}: {val}')
        print()
    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(my_contacts)
        elif choice == ADD:
            add(my_contacts)
        elif choice == CHANGE:
            change(my_contacts)
        elif choice == DELETE:
            delete(my_contacts)
    save_contacts(my_contacts)


def load_contacts():
    try:
        input_file = open(FILENAME,'rb')
        contact_dct = pickle.load(input_file)
    except IOError: #jesli plik nie zostanie znaleziony
        contact_dct = {}
    return contact_dct

def get_menu_choice():
    print('Menu:')
    print('--------------------')
    print('1.Wyszukanie osoby')
    print('2.Dodanie nowej osoby.')
    print('3.Zmiana danych isteniejącej osoby.')
    print('4.Skasowanie istniejącej osoby.')
    print('5.Koniec programu')

    choice = int(input('Wybierz opcje: '))
    while choice < LOOK_UP or choice > QUIT:
        print('Wybierz poprawną opcję: ')
    return choice

def look_up(dict_contacts):
    name = input('Podaj imie i nazwisko: ')
    print(dict_contacts.get(name, 'Nie znaleziono osoby.'))
    if name in dict_contacts:
        print(name)
    else:
        print('Osoba nie istnieje.')

def add(dict_contacts):
    name = input('Podaj imię i nazwisko: ')
    phone = input('Podaj numer telefonu: ')
    email = input('Podaj email: ')

    entry = contacts.Contacts(name,phone,email)

    if name not in dict_contacts:
        dict_contacts[name] = entry
        print('Osoba została dodana.')
    else:
        print('Podana osoba już istnieje.')
    save_contacts(dict_contacts)
    print()

def change(dict_contacts):
    name = input('Podaj imię i nazwisko: ')
    if name in dict_contacts:
        phone = input('Podaj nr telefonu: ')
        email = input('Podaj email: ')

        entry = contacts.Contacts(name,phone,email)
        dict_contacts[name] = entry
        print('Informacje zostały uaktualnione.')

    else:
        print('Nie znaleziono osoby.')

def delete(dict_contacts):
    name = input('Podaj imię i nazwisko: ')
    if name in dict_contacts:
        del dict_contacts[name]
        print(f'Imie {name} zostało usunięte.')
    else:
        print('Imię nie zostało znalezine.')

def save_contacts(dict_contacts):
    output_file = open(FILENAME,'ab')
    pickle.dump(dict_contacts,output_file)
    output_file.close()

main()



























