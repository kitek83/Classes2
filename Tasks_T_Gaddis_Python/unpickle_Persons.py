import pickle

file = open('Persons.dat','rb')
persons = pickle.load(file)
print(persons)
print('----------------------')

for person in persons:
    print(f'Name and surname: {person.get_name()}')

    print(f'Address: {person.get_address()}')

    print(f'Age: {person.get_age()}')

    print(f'Phone nr: {person.get_phone()}')

    print()