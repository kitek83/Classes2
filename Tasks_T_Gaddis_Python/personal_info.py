#task 3_page_577_Tonny_Gaddis
class Personal:
    def __init__(self,name,address,age,phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def set_name(self,name):
        self.name = name
    def set_address(self,address):
        self.address = address
    def set_age(self,age):
        self.age = age
    def set_phone(self,phone):
        self.phone = phone

    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_age(self):
        return self.age
    def get_phone(self):
        return self.phone

