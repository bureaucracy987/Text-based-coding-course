from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(animal):
    def move(self):
        print("I can walk and run.")
class Snake(animal):
    def move(self):
        print("I can crawl.")
class Lion(animal):
    def move(self):
        print("I can roar.")
class Bird(animal):
    def move(self):
        print("I can fly.")
R=Human()
R.move()
K=Snake()
K.move()
Z=Lion()
Z.move()
a=Bird()
a.move()
