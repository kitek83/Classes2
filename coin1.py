import random
class Coin:
    def __init__(self):  #metoda __init__ inicjalizuje atrybut danych sideup o wartości 'orzel'
        self.sideup = 'orzel'

    #symulacja rzutu moneta
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'orzel'
        else:
            self.sideup = 'reszka'
    #metoda get_sideup zwraca wartosc przechowywana przez atrybut danych sideup
    def get_sideup(self):
        return self.sideup

def main():
    #utworzenie obiektu klasy Coin
    my_coin = Coin()

    print(f'wynik rzutu moneta: {my_coin.get_sideup()}')
    print('Symulacja rzutu moneta:...')
    my_coin.toss()
    print(f'Wynik rzutu moneta: {my_coin.get_sideup()}')



main()