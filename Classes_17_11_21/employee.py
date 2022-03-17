class Employee:
    def __init__(self,surname,id):
        self.surname = surname
        self.id = id
    
    def set_surname(self,surname):
        self.surname = surname
    def set_id(self,id):
        self.id = id
    
    def get_surname(self):
        return self.surname
    def get_id(self):
        return self.id

class ProductionWorker(Employee):
    def __init__(self,surname,id,nr,rate):
        Employee.__init__(self,surname,id)
        self.change_nr = nr
        self.hour_rate = rate

    def set_change_nr(self,nr):
        self.change_nr = nr
    def hour_rate(self,rate):
        self.hour_rate = rate

    def get_change_nr(self):
        return self.change_nr
    def get_hour_rate(self):
        return self.hour_rate
