import pet

def main():
    name = input('Enter the name of your pet: ')
    type = input('Enter the type of your pet: ')
    age = int(input('Enter the age of your pet: '))

    my_pet = pet.Pet(name,type,age)

    print('You entered the following data related with the pet: ')

    print(f'Name of the pet: {my_pet.get_name()}')
    print(f'Type of the pet: {my_pet.get_type()}')
    print(f'Age: {my_pet.get_age()}')


main()