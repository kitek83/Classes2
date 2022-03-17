#ten program przeprowadza serializację obiektów klasy Phone z pliku cellphone.py

import pickle
import cellphone

FILNAME = 'cellphone.dat'

def main():
    again = 't'
    while again == 't':
        output_file = open(FILNAME, 'ab')

        man = input('Podaj producenta: ')
        mod = input('Podaj model: ')
        price = float(input('Podaj cenę: '))
        phone = cellphone.Phone(man, mod, price)

        pickle.dump(phone, output_file)

        again = input('Czy chcesz wprowadzać dalej dane telefonu (t/n?): ')

        output_file.close()
        print(f'Dane zostały zapisane w pliku {FILNAME}.')


main()