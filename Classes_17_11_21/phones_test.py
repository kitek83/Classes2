import phones
import pickle

FILENAME = 'phones.dat'
def main():
    phones_list = make_list()
    print('O to wprowadzone przez Ciebie dane: ')
    display_phones(phones_list)

def make_list():
    phone_s = []
    count = 0
    file = open(FILENAME,'ab')
    for counter in range(1,4):
        count += 1
        man = input(f'Podaj producenta telefonu nr{count}: ')
        mod = input(f'Podaj model telefonu nr {count}: ')
        price = float(input(f'Podaj cenę telefonu nr {count}: '))
        print()

        phone = phones.Phones(man,mod,price)
        #adding object to the list
        phone_s.append(phone)
    pickle.dump(phone_s,file)
    return phone_s

def display_phones(phone_ss):
    for item in phone_ss:
        print(f'Producent telefonu: {item.get_manufacture()}')
        print(f'Model telefonu: {item.get_model()}')
        print(f'Cena telefonu: {item.get_price()}')

main()