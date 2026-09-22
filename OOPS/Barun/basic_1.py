class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        print(self.brand, "car created")
        Car.total_cars += 1                     

    def describe(self):                     # instance method
        return f"This is a {self.brand}"

    @classmethod
    def car_count(cls):                     # class method
        return f"Total cars made: {cls.total_cars}"

    @staticmethod
    def is_valid_brand(name):               # static method
        return isinstance(name, str) and len(name) > 0

car1 = Car("Toyota")  
car2 = Car("Honda")

print(car1.describe())          # This is a Toyota
print(Car.car_count())          # Total cars made: 2
print(Car.is_valid_brand("BMW"))  # True








