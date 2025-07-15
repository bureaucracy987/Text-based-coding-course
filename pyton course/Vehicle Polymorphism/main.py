class Mahindra_XUV_3XO():
    def company(self):
        print("The company is Mahindra")
    def price(self):
        print("The price ranges from 7.99 lakhs to 15.80 lakhs.")
    def fuel(self):
        print("This car runs on petrol.")
class Kia_Carens_Claven_EV():
    def company(self):
        print("The company is Kia")
    def price(self):
        print("The price starts from 22.00 lakhs.")
    def fuel(self):
        print("This car runs on electricity.")
class Mahindra_Thar_ROXX():
    def company(self):
        print("The company is Mahindra")
    def price(self):
        print("The price ranges from 12.99 to 23.39 lakhs.")
    def fuel(self):
        print("This car runs on diesel.")
obj_Mah=Mahindra_XUV_3XO()
obj_Kia=Kia_Carens_Claven_EV()
obj_Mah2=Mahindra_Thar_ROXX()
for car in(obj_Mah,obj_Kia,obj_Mah2):
    car.company()
    car.price()
    car.fuel()
    
