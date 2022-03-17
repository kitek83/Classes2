import cellphone

def main():
    phones = make_list()
    print('O to wprowadzone przez Ciebie dane: ')
    display_phones(phones)

def make_list():
    phones_list = []

    for num in range(1,4):
        man = input(f'{num}.Podaj producenta:')
        model = input(f'{num}Podaj model:')
        cena = float(input(f'{num}Podaj cene: '))
        phone = cellphone.Phone(man,model,cena)
        phones_list.append(phone)
    return phones_list

def display_phones(phones_list):

    file = open('phones.txt', 'w') #I tries to save data in txt file, but sth is wrong
    for item in phones_list:
        print(item.get_manufact())
        file.write(str(item.get_manufact()))
        print(item.get_model())
        file.write(str(item.get_model()))
        print(item.get_price())
        file.write(str(item.get_price()))
        print()


main()