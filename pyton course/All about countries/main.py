class India():
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is spoken primarily in India.")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington DC is the capital of USA.")
    def language(self):
        print("English is spoken in USA.")
    def type(self):
        print("USA is a developed country.")
obj_ind=India()
obj_usa=USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()