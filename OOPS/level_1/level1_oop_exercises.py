"""
Level 1 — OOP Foundations: Exercises
Fill in each TODO. Run the file - the asserts will tell you if you got it right.
Don't peek at level1_oop_practice.py while solving these; try from memory first.

    python level1_oop_exercises.py
"""

# ---------------------------------------------------------------------------
# Exercise 1 — Classes, objects, __init__, self
# ---------------------------------------------------------------------------
# Create a `Book` class with:
#   - __init__ that accepts title (str) and pages (int), stored as instance attributes
#   - a method `summary(self)` that returns "'<title>' has <pages> pages"

# TODO: define the Book class here


# --- checks (do not edit below) ---
book1 = Book("Clean Code", 464)
book2 = Book("Fluent Python", 792)
assert book1.title == "Clean Code"
assert book2.pages == 792
assert book1.summary() == "'Clean Code' has 464 pages"
print("Exercise 1 passed!")


# ---------------------------------------------------------------------------
# Exercise 2 — Class attributes vs instance attributes
# ---------------------------------------------------------------------------
# Create a `Library` class with:
#   - a CLASS attribute `total_books` starting at 0
#   - __init__ that accepts a name (str), stores it as an instance attribute,
#     and increments Library.total_books by 1 every time a new Library is created

# TODO: define the Library class here


# --- checks ---
lib1 = Library("City Library")
lib2 = Library("School Library")
assert Library.total_books == 2
assert lib1.name == "City Library"
print("Exercise 2 passed!")


# ---------------------------------------------------------------------------
# Exercise 3 — Instance method, class method, static method
# ---------------------------------------------------------------------------
# Create a `TemperatureLog` class with:
#   - __init__ that accepts a city (str) and a list of temperature readings
#   - an INSTANCE method `average(self)` returning the average of self.readings
#   - a STATIC method `to_fahrenheit(celsius)` converting celsius -> fahrenheit
#     formula: F = C * 9/5 + 32
#   - a CLASS method `from_single_reading(cls, city, temp)` that returns a new
#     TemperatureLog for that city with just one reading in the list

# TODO: define the TemperatureLog class here


# --- checks ---
log1 = TemperatureLog("Kolkata", [30, 32, 31])
assert log1.average() == 31
assert TemperatureLog.to_fahrenheit(0) == 32
log2 = TemperatureLog.from_single_reading("Delhi", 40)
assert log2.readings == [40]
assert log2.city == "Delhi"
print("Exercise 3 passed!")


# ---------------------------------------------------------------------------
# Exercise 4 — Mutable default trap (spot the bug, then fix it)
# ---------------------------------------------------------------------------
# The class below has the classic shared-mutable-class-attribute bug.
# Fix ShoppingCart so that each instance gets its OWN independent `items` list.

class ShoppingCart:
    items = []   # <-- bug is here

    def __init__(self, owner):
        self.owner = owner

    def add_item(self, item):
        self.items.append(item)


# TODO: fix the class above (edit it directly)

# --- checks ---
cart1 = ShoppingCart("Raju")
cart2 = ShoppingCart("Priya")
cart1.add_item("Laptop")
assert cart2.items == [], f"Expected empty cart for Priya, got {cart2.items}"
print("Exercise 4 passed!")


# ---------------------------------------------------------------------------
# Exercise 5 — Object identity vs equality
# ---------------------------------------------------------------------------
# Without writing any code: answer in a comment below.
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
#
# TODO: In a comment, answer:
#   a) Will `p1 == p2` be True or False by default, and why?
#   b) Will `p1 is p2` be True or False, and why?
#   c) What would you need to add to the Point class to make `p1 == p2` return True?
#      (You don't need to implement it yet - just name the special method involved.
#       We'll build it properly in Level 5: Polymorphism.)


print("\nAll done! Review your Exercise 5 answers, then let's discuss.")
