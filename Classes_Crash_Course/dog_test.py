import dog

def main():
  my_dog = dog.Dog('Willy',6)
  your_dog = dog.Dog('Lucy',8)

  print(f'My dog name is {my_dog.name}.')
  print(f'My dog age is {my_dog.age}.')
  my_dog.sit()
  my_dog.roll_over()
  print()

  print(f'Your dog name is {your_dog.name}.')
  print(f'Your dig age is {your_dog.age}.')
  your_dog.sit()
  your_dog.roll_over()




main()