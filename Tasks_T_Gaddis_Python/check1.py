import employee
import pickle

load_file = open('Employee.dat','rb')
file_pickle  = pickle.load(load_file)

print(file_pickle)

for key,val in file_pickle.items():
    print(f'{key}: {val.get_name(), val.get_identity_nr(), val.get_department(), val.get_position()}')
print()
print('-------------------------')

identity = int(input('Enter identity nr of the worker: '))
for key, val in file_pickle.items():
    if identity == key:
        print(f'{val.get_name(),val.get_identity_nr(),val.get_department(),val.get_position()}')
