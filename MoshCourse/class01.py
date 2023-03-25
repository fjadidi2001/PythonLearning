class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


fateme = Person("Fatemeh Jadidi")
print(fateme.name)
fateme.talk()
