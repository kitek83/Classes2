class Phones:
    def __init__(self,manufacture,model,price):
        self.manufacture = manufacture
        self.model = model
        self.price = price

    def set_manufacture(self,manufacture):
        self.manufacture = manufacture
    def set_model(self,model):
        self.model = model
    def set_price(self,price):
        self.price = price

    def get_manufacture(self):
        return self.manufacture
    def get_model(self):
        return self.model
    def get_price(self):
        return self.price