class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0              #this is atribute, which is not being passed as parameter

    def car_describe(self):
        long_name = f'{self.make},\n{self.model},\n{self.year}'
        return long_name.title()

    def odometer_reading(self):
        print(f'The car has {self.odometer} Miles done.')

    def odmeter_update(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back the odommeter.")

    def increment_odometer(self,miles):
        self.miles = miles
        self.odometer += miles
        return miles

def main():
   my_car = Car('audi','a4','2004')
   print(my_car.car_describe())
   print()
   my_car.odmeter_update(150)
   my_car.odometer_reading()
   print(f'{my_car.car_describe()} drove {my_car.increment_odometer(55)} Miles.')
   #my_car.increment_odometer(55)
   my_car.odometer_reading()


main()