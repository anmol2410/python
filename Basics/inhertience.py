# Parent class
class Cars: 
    def wheel_type(self):
        print("4x4")

class Gwagon(Cars):
    def price(self):
        print("Higher")

class Thar(Cars):
    pass

car1=Gwagon()
car1.wheel_type()
car1.price()

car2=Thar()
car2.wheel_type()


