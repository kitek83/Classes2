class Restaurant:
    def __init__(self,name,cousine_type):
        self.name = name
        self.cousine_type = cousine_type

    def describe_restaurant(self):
        print(f'Restaurant {self.name} offers {self.cousine_type} cousine types.')

    def open_restaurant(self):
        print('Restaurant is opened from 1000 to 2200.')


def main():
    restaurant = Restaurant('Filicina','Italian, Polish')
    restaurant.describe_restaurant()
    print()
    print(f'Restuarant name is {restaurant.name}.')
    print(f'Resturant offers {restaurant.cousine_type} cousine types.')
    restaurant.open_restaurant()
    print()
    restaurant2 = Restaurant('Polska Chata','Plish, German')
    restaurant2.describe_restaurant()
    restaurant2.open_restaurant()
    print()
    restaurant3 = Restaurant('Chinese Street','Chinese, Vietnam')
    restaurant3.describe_restaurant()
    restaurant3.open_restaurant()

main()