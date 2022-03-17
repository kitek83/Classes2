#task_1_page_576
class Pet:
    def __init__(self,name,type,age):
        self.name = name
        self.animal_type = type
        self.age = age

    def set_name(self,name):
        self.name = name
    def set_type(self,type):
        self.animal_type = type
    def set_age(self,age):
        self.age = age

    def get_name(self):
        return self.name
    def get_type(self):
        return self.animal_type
    def get_age(self):
        return self.age
