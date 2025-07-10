class Myclass:
    __privateVar=27
    def hello(self):
        print("Private Variable Value:",Myclass.__privateVar)
foo=Myclass()
foo.hello()