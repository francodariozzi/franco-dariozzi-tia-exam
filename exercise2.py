class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def make_sound(self):
        print(self.name, "says: Woof!")

class Cat(Animal):
    def make_sound(self):
        print(self.name, "says: Meow!")

dog = Dog("Buddy", "Woof")
cat = Cat("Whiskers", "Meow")

dog.make_sound()
cat.make_sound()
