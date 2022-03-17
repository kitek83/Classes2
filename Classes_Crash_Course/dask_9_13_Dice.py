from random import randint
class Die:
    def __init__(self,sides):
        self.sides = sides

    def roll_die(self):

        if self.sides == 6:
            c = 0
            print('6 sided die will be rolled 6 times')
            for roll in range(6):
                c += 1
                result = randint(1,6)
                print(f'{c}roll:{result}')
            print()
        elif self.sides == 10:
            c = 0
            print('10 sided die will be rolled 10 times.')
            for roll in range(10):
                c += 1
                result = randint(1,10)
                print(f'{c} roll: {result}')
            print()
        elif self.sides == 20:
            c = 0
            print('20 sided die will be rolled 10 times.')
            for roll in range(10):
                c += 1
                result = randint(1,20)
                print(f'{c} roll: {result}')
            print()
def main():
   die1 = Die(6)
   die2 = Die(10)
   die3 = Die(20)

   die1.roll_die()
   print()
   die2.roll_die()
   print()
   die3.roll_die()

main()



