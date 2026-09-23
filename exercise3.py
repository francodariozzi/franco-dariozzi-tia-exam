class Hero:
    def __init__(self, name, power):
        self.name = name
        self.__power = power

    def get_power(self):
        return self.__power


class Villain:
    def __init__(self, name, power):
        self.name = name
        self.__power = power

    def get_power(self):
        return self.__power


class SuperHero(Hero):
    def display_info(self):
        print("Hero:", self.name)
        print("Power:", self.get_power())
        print(self.name, "uses their power to save people!")


class SuperVillain(Villain):
    def display_info(self):
        print("Villain:", self.name)
        print("Power:", self.get_power())
        print(self.name, "uses their power to cause trouble!")

hero_name = input("Enter the hero's name: ")
hero_power = input("Enter the hero's power: ")

villain_name = input("Enter the villain's name: ")
villain_power = input("Enter the villain's power: ")

hero = SuperHero(hero_name, hero_power)
villain = SuperVillain(villain_name, villain_power)

print("Character Details")
hero.display_info()
print()
villain.display_info()
