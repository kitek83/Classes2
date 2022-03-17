import animals
def main():
    mammal = animals.Mammal('zwierzę')
    dog = animals.Dog()
    cat = animals.Cat()

    show_animals(mammal)
    print()
    show_animals(dog)
    print()
    show_animals(cat)

def show_animals(creature):
    creature.show_species()
    creature.make_sound()



main()