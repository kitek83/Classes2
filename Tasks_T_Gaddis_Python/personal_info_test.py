import personal_info
import pickle
def main():
    person1 = personal_info.Personal('Kris Kozak','Fińska 17/2','38','732-939-996')
    person2 = personal_info.Personal('Patryk Rojek', 'Pokoju 37','39','543-333-321')
    person3 = personal_info.Personal('Jacek Mencel','Okolna 23','38','434-332-222')

    persons = [person1,person2,person3]

    file = open('Persons.dat','wb')
    pickle.dump(persons,file)


    for person in persons:
        print(f'Name and surname: {person.get_name()}')

        print(f'Address: {person.get_address()}')

        print(f'Age: {person.get_age()}')

        print(f'Phone nr: {person.get_phone()}')

        print()


main()