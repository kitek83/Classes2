class Contacts:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def set_name(self,name):
        self.name = name
    def set_phone(self,phone):
        self.phone = phone
    def set_email(self,email):
        self.email = email

    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def get_email(self):
        return self.email

    #Metoda __str()__ zwraca ciag tekstowy przedstawiajacy informacje o stanie obiektu
    def __str__(self):
        return 'imię i nzwisko: ' + self.name +\
            '\nNumer telefonu: ' + self.phone +\
            '\nAdres e-mail: ' + self.email
