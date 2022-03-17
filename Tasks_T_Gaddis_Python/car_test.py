import car
def main():
    car1 = car.Car(2008,'Peguot SW',0)

    print('Dates are related with: ')
    print(f'Model: {car1.get_make()}')
    print(f'Production year: {car1.get_year()}')
    print()
    print(f'The speed of car is: {car1.get_speed()}')
    print('Accelerate1:')
    car1.accelerate()
    print(f'Actual speed: {car1.get_speed()}')
    print('Accelerate2:')
    car1.accelerate()
    print(f'Actual speed is: {car1.get_speed()}')
    print('Accelerate3: ')
    car1.accelerate()
    print(f'Actual speed is: {car1.get_speed()}')

    print()
    print('Break1:')
    car1.brake()
    print(f'Actual speed is: {car1.get_speed()}')
    print('Break2: ')
    car1.brake()
    print(f'Actual speed is: {car1.get_speed()}')

main()