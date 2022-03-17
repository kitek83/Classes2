class Car:
    def __init__(self,year,make,speed):
        self.year = year
        self.make = make
        self.speed = speed

    def set_speed(self,speed):
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def set_year(self,year):
        self.year = year
    def set_make(self, make):
        self.make = make

    def get_year(self):
        return self.year
    def get_make(self):
        return self.make

    def get_speed(self):
        return self.speed
