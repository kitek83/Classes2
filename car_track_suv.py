import vehicles

def main():
    car = vehicles.Car('BMW',2001,70000,15000.0,4)
    track = vehicles.Track('Toyota',2002,40000,12000.0,'4WD')
    suv = vehicles.Suv('Volvo',2000,30000,18500.0,5)

    print('Dostępne samochody używane: ')
    print('============================')
    print('W ofercie jest następujący samochód używany: ')
    print(f'Marka: {car.get_make()}')
    print(f'Model: {car.get_model()}')
    print(f'Przebieg {car.get_mileage()}')
    print(f'Cena: {car.get_price()}')
    print(f'Liczba drzwi: {car.get_doors()}')
    print()

    print('Dostępne samochody używane: ')
    print('============================')
    print('W ofercie jest następujący samochód używany: ')
    print(f'Marka: {track.get_make()}')
    print(f'Model: {track.get_model()}')
    print(f'Przebieg {track.get_mileage()}')
    print(f'Cena: {track.get_price()}')
    print(f'Liczba drzwi: {track.get_drive_type()}')
    print()

    print('Dostępne samochody używane: ')
    print('============================')
    print('W ofercie jest następujący samochód używany: ')
    print(f'Marka: {suv.get_make()}')
    print(f'Model: {suv.get_model()}')
    print(f'Przebieg: {suv.get_mileage()}')
    print(f'Cena: {suv.get_price()}')
    print(f'Liczba drzwi: {suv.get_pass_cap()}')
    print()

main()