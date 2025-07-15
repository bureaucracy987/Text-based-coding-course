class Fish:
    def __init__(self):
        self.__maxprice=1000
    def sell(self):
        print("Selling price is:{}".format(self.__maxprice))
    def setMaxprice(self, price):
        self.__maxprice=price
c=Fish()
c.sell()
c.__maxprice=626
c.sell()
c.setMaxprice(45670)
c.sell()