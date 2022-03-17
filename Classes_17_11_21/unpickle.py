import pickle

file = open('phones.dat','rb')
phones = pickle.load(file)

print(phones)

for item in phones:
    print(item.get_manufacture())
    print(item.get_model())
    print(item.get_price())
    print()

