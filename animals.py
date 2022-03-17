#polimorfizm
class Mammal:
    def __init__(self,species):
        self.species = species

    def show_species(self):
        print(f'To jest {self.species}')

    def make_sound(self):
        print('Grrrr')

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self,'pies')

    def make_sound(self):
        print('Hau!,Hau!')

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self,'Cat')

    def make_sound(self):
        print('Miau, Miau')