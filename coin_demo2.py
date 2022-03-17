import coin
def main():
    #utworzenie 3ech egzemplarzy klasy Coin
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    print('O to wyniki rzutów 3ema monetami: ')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    
    print()
    print('Symulacja rzutu 3ema monetami...')
    coin1.toss()
    coin2.toss()
    coin3.toss()
    
    print()
    print('O to wyniki rzutów 3ema monetami: ')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    



main()