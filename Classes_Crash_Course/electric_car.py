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

class Battery:
    def __init__(self,battery_size=100):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has {self.battery_size} - kWh battery.')

    def range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 320
        print(f'This car can go {range} on fully charged battery.')

class Electric(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


def main():
   my_car = Car('audi','a4','2004')
   print(my_car.car_describe())
   print()
   my_car.odmeter_update(150)
   my_car.odometer_reading()
   print(f'{my_car.car_describe()} drove {my_car.increment_odometer(55)} Miles.')
   #my_car.increment_odometer(55)
   my_car.odometer_reading()

   print(3*'------------------------------')
   my_tesla = Electric('tesla','model s','2016')
   print(my_tesla.car_describe())
   my_tesla.battery.describe_battery()
   my_tesla.battery.range()



main()