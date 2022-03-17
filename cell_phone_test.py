import cellphone

man = input('Enter manufacturer of the phone: ')
model = input('Enter model of the phone: ')
price = float(input('Enter price of the phone: '))

phone = cellphone.Phone(man,model,price)

print('Oto podane przec ciebie dane: ')
print(f'Producent: {phone.get_manufact()}')
print(f'Model: {phone.get_model()}')
print(f'cena: {phone.get_price()}')

