import employee

def main():
    surn = input('Enter Your surname: ')
    id = input('Enter Your id: ')
    chan_nr = int(input('Enter Your change nr (1 or 2): '))
    hr_rate = float(input('Enter Your hourly rate: '))

    worker = employee.ProductionWorker(surn,id,chan_nr,hr_rate)
    print()
    print('Here are data you have entered: ')
    print(f'Surname: {worker.get_surname()}')
    print(f'Id nr: {worker.get_id()}')
    print(f'Change nr: {worker.get_change_nr()}')
    print(f'Hourly rate: {worker.get_hour_rate()}')


main()