class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=Parrot("Blu",56)
woo=Parrot("woo",12)
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))


