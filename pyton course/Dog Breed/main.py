class Dog:
    species="mammal"
    def __init__(self,breed,lifespan,name):
        self.breed=breed
        self.lifespan=lifespan
        self.name=name
Ronny=Dog("pug",14,"Ronny")
Boldy=Dog("Alsation",11,"Boldy")
Cutey=Dog("Poodle",12,"Cutey")
print("{} is a {},his breed is {}, and his lifespan is {} years. ".format(Ronny.name,Ronny.species,Ronny.breed,Ronny.lifespan))       
print("{} is a {},his breed is {}, and his lifespan is {} years. ".format(Boldy.name,Boldy.species,Boldy.breed,Boldy.lifespan))       
print("{} is a {},his breed is {}, and his lifespan is {} years. ".format(Cutey.name,Cutey.species,Cutey.breed,Cutey.lifespan))       

