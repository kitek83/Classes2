class User:
    def __init__(self,first_name,last_name,age,job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Job: {self.job}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}!')

    def increment_login_attempts(self,login):
        self.login = login
        self.login_attempts += login

        return self.login_attempts

    def reset_loggin_attempts(self,reset):
        self.login = reset
        self.login_attempts -= reset
        return self.login_attempts

def main():
    user1 = User('Kris','Kozak',38,'Programmer')
    user1.describe_user()

    print(f'Login attempts: {user1.increment_login_attempts(1)}.')
    print(f'Login attempts: {user1.increment_login_attempts(1)}.')
    print(f'User1 has login attempts: {user1.login_attempts}.')
    print('User 1 made reset of login attempt:')
    print(f'After reset login attempts: {user1.reset_loggin_attempts(1)}.')
    print(f'User1 has login attempts: {user1.login_attempts}.')

main()