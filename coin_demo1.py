import coin

my_coin = coin.Coin()
print('Wynik rzutu moneta: ',my_coin.get_sideup())
print('Symulacja 10 ciu rzutow moneta...')

for count in range(10):
    my_coin.toss()
    print(my_coin.get_sideup())
