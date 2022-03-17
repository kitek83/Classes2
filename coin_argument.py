#ten program przekazuje obiekt Coin jako argument funkcji
import coin

def main():
    my_coin = coin.Coin()
    print(my_coin.get_sideup())
    flip(my_coin)                 #object was passek like an argument
    print(my_coin.get_sideup())

def flip(coin_obj):
    coin_obj.toss()

main()
