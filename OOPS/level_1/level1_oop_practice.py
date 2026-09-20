"""
Level 1 — OOP Foundations: Practice / Demo file
Run this file section by section (or the whole thing) and READ the printed output.
Matches level1_oop_theory.md — same section numbers.

    python level1_oop_practice.py
"""

print("=" * 60)
print("1. CLASSES AND OBJECTS")
print("=" * 60)


class Car:
    pass


car1 = Car()
car2 = Car()
print("car1 is car2:", car1 is car2)   # False -> two separate objects


print("\n" + "=" * 60)
print("2. __init__ AND 3. self")
print("=" * 60)


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def honk(self):
        # 'self' here is whichever car object called honk()
        print(f"{self.brand} ({self.color}) says beep!")


car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.honk()
car2.honk()

# Proof that car1.honk() is really Car.honk(car1) under the hood:
Car.honk(car1)   # identical result to car1.honk()


print("\n" + "=" * 60)
print("4. INSTANCE ATTRIBUTES VS CLASS ATTRIBUTES")
print("=" * 60)


class Car:
    wheels = 4  # class attribute - shared

    def __init__(self, brand):
        self.brand = brand  # instance attribute - per object


car1 = Car("Toyota")
car2 = Car("Honda")
print("Before:", car1.wheels, car2.wheels)

Car.wheels = 6  # change on the CLASS
print("After changing via class:", car1.wheels, car2.wheels)

car1.wheels = 3  # this creates an INSTANCE attribute that shadows the class one
print("After car1 gets its own wheels:", car1.wheels, car2.wheels)
# Notice car2.wheels is still 6 -> car1 now has its own private copy


print("\n" + "=" * 60)
print("5. INSTANCE / CLASS / STATIC METHODS")
print("=" * 60)


class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    def describe(self):                       # instance method
        return f"This is a {self.brand}"

    @classmethod
    def car_count(cls):                       # class method
        return f"Total cars made: {cls.total_cars}"

    @staticmethod
    def is_valid_brand(name):                 # static method
        return isinstance(name, str) and len(name) > 0


car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.describe())
print(Car.car_count())
print("Is 'BMW' valid?", Car.is_valid_brand("BMW"))
print("Is '' valid?", Car.is_valid_brand(""))


print("\n" + "=" * 60)
print("6. OBJECT IDENTITY")
print("=" * 60)

car1 = Car("Toyota")
car2 = Car("Toyota")

print("car1 == car2:", car1 == car2)   # False (default equality = identity, until customized)
print("car1 is car2:", car1 is car2)   # False
print("id(car1):", id(car1))
print("id(car2):", id(car2))


print("\n" + "=" * 60)
print("7. MUTABLE VS IMMUTABLE ATTRIBUTES")
print("=" * 60)


class GoodCar:
    def __init__(self, brand):
        self.brand = brand
        self.features = []  # new list created PER INSTANCE, inside __init__


c1 = GoodCar("Toyota")
c2 = GoodCar("Honda")
c1.features.append("Sunroof")
print("Good design -> c1.features:", c1.features, "| c2.features:", c2.features)


class BadCar:
    features = []  # DANGER: one shared list for every instance

    def __init__(self, brand):
        self.brand = brand


b1 = BadCar("Toyota")
b2 = BadCar("Honda")
b1.features.append("Sunroof")
print("Bad design  -> b1.features:", b1.features, "| b2.features:", b2.features)
print("^ b2 got the sunroof too! This is the classic mutable-class-attribute trap.")


print("\n" + "=" * 60)
print("8. BASIC ENCAPSULATION")
print("=" * 60)


class Car:
    def __init__(self, brand):
        self.brand = brand              # public
        self._vin = "HIDDEN123"         # protected (convention only)
        self.__engine_code = "X9"       # name-mangled


car1 = Car("Toyota")
print("public:", car1.brand)
print("protected (still accessible):", car1._vin)
try:
    print(car1.__engine_code)
except AttributeError as e:
    print("AttributeError as expected:", e)
print("mangled name still reachable:", car1._Car__engine_code)


print("\n" + "=" * 60)
print("Done. Now open level1_oop_exercises.py and complete the TODOs.")
print("=" * 60)
