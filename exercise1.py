class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print("Brand:", self.brand)
        print("Year:", self.year)

vehicle1 = Vehicle("Toyota", 2020)
vehicle2 = Vehicle("Ford", 2023)

vehicle1.display_info()
vehicle2.display_info()
