class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'The dog {self.name} is sitting now.')

    def roll_over(self):
        print(f'The dog {self.name} is rolling over.')
