#Task_4_page_577_T_Gaddis
class Employee():
    def __init__(self,name,identity_nr,department,position):
        self.name = name
        self.identity_nr = identity_nr
        self.department = department
        self.position = position

    def set_name(self,name):
        self.name = name
    def set_identity_nr(self,identity_nr):
        self.identity_nr = identity_nr
    def set_department(self,department):
        self.department = department
    def set_position(self,position):
        self.position = position

    def get_name(self):
        return self.name
    def get_identity_nr(self):
        return self.identity_nr
    def get_department(self):
        return self.department
    def get_position(self):
        return self.position