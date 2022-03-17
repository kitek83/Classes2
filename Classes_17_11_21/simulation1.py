import random
#try to simulat a dice roll with the use of classes
class DiceRoll:
    def __init__(self):
        self.roll = 'one'

    def toss(self):
        if random.randint(1,6) == 1:
            self.roll = 'one'
        elif random.randint(1,6) == 2:
            self.roll = 'two'
        elif random.randint(1,6) == 3:
            self.roll = 'three'
        elif random.randint(1,6) == 4:
            self.roll = 'four'
        elif random.randint(1,6) == 5:
            self.roll = 'five'
        elif random.randint(1,6) == 6:
            self.roll = 'six'
        return self.roll

    def get_roll(self):
        return self.roll

def main():
    #creating object
    dice = DiceRoll()
    print(f'Wynik rzutu kostką: {dice.get_roll()}')
    print()
    print(f'Symulacja rzutu kostką: {dice.toss()} ')
    print()
    print(f'Wynik rzutu kostką: {dice.get_roll()}')

main()
