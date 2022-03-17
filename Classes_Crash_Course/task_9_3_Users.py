class User:
    def __init__(self,first_name,last_name,age,job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def describe_user(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Job: {self.job}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')