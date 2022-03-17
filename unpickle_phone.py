#Ten program przeprowadza deserializacje obiektów klasy Phone
import cellphone
import pickle

FILENAME = 'cellphone.dat'

def main():
    end_of_file = False
    input_file = open(FILENAME,'rb')

    while not end_of_file:
        try:
            file = pickle.load(input_file)
            display(file)
        except EOFError:
            end_of_file = True
    input_file.close()

def display(file):
    print(f'Producent: {file.get_manufact()}')
    print(f'Model: {file.get_model()}')
    print(f"Cena: {format(file.get_price(),'.2f')}")
    print()

main()

