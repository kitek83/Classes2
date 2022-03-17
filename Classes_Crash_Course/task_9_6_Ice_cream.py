class Restaurant:
    def __init__(self, name, cousine_type):
        self.name = name
        self.cousine_type = cousine_type
        self.number_surved = 0

    def describe_restaurant(self):
        print(f'Restaurant {self.name} offers {self.cousine_type} cousine types.')

    def open_restaurant(self):
        print('Restaurant is opened from 1000 to 2200.')

    def set_number_served(self, customers):
        self.customers = customers
        return customers
class IceCreamStand(Restaurant):
    def __init__(self,name,cousine_type,flavors):
        super().__init__(name,cousine_type)
        self.flavors = flavors

    def dis_flavors(self,flavors):
        self.flavors = flavors
        print(f'We offer the following flavors: {self.flavors}.')


def main():
    restaurant = Restaurant('Filicina', 'Italian, Polish')
    restaurant.describe_restaurant()
    print(f'Restaurant {restaurant.name} has served {restaurant.set_number_served(18)} customers.')
    print()
    print(f'Restuarant name is {restaurant.name}.')
    print(f'Resturant offers {restaurant.cousine_type} cousine types.')
    restaurant.open_restaurant()
    print()
    restaurant2 = Restaurant('Polska Chata', 'Plish, German')
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    print()
    restaurant3 = Restaurant('Chinese Street', 'Chinese, Vietnam')
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()
    print(2*'--------------------------------------------------')
    ice_cream = IceCreamStand('','',['vanilla','strawbery','chocolate'])
    ice_cream.dis_flavors(['vanilla','strawbery','chocolate'])




main()