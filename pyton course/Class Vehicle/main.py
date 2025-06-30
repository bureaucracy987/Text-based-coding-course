class Vehicle:
    def __init__(self,max_speed,mileage ):
        self.max_speed=max_speed
        self.mileage=mileage
modelx=Vehicle(240,18)
modely=Vehicle(340,56)
print("Model 1 Max Speed:",modelx.max_speed)
print("Model 1 Mileage:",modelx.mileage)
print("Model 2 Max Speed:",modely.max_speed)
print("Model 2 Mileage:",modely.mileage)
