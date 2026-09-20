# Level 1 — OOP Foundations (Theory)

> Companion files: `level1_oop_practice.py` (runnable demos) and `level1_oop_exercises.py` (your turn).
> Read a section here, then run the matching demo in the practice file before moving on.

---

## 1. Classes and Objects

**Simple explanation:**
A **class** is a blueprint — it describes what something *has* (attributes) and what it *can do* (methods), but it is not the thing itself. An **object** (also called an *instance*) is a real thing built from that blueprint, with its own actual data.

**Analogy:**
`class Car` is the architectural blueprint for a car — dimensions, engine type, how the wheels work. It's not drivable. `my_car = Car()` is an actual car built from that blueprint, sitting in your driveway, with its own license plate and fuel level.

**Key idea:** one class → many independent objects, each with its own state.

```python
class Car:
    pass

car1 = Car()
car2 = Car()
print(car1 is car2)   # False — two separate objects, same blueprint
```

**Common mistakes:**
- Thinking the class itself stores an object's data — it doesn't. The class defines *structure*; each object holds its *own* data.
- Confusing "class" (the blueprint) with "object" (a specific instance) when talking through a design.

---

## 2. `__init__` — the Initializer

**Simple explanation:**
`__init__` is a special method Python automatically calls right after an object is created. It's where you set up the object's starting state — its initial attribute values.

**Analogy:**
Think of `__init__` as the factory setup checklist that runs the moment a car rolls off the assembly line: "install this engine, paint it this color, set the odometer to 0."

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
print(car1.brand)   # Toyota
print(car1.color)   # Red
```

**Line-by-line:**
- `def __init__(self, brand, color):` — defines the setup method; it takes `self` plus whatever data you want to pass in when creating the object.
- `self.brand = brand` — stores the passed-in value onto *this specific object*.
- `Car("Toyota", "Red")` — Python calls `__init__` automatically with `self` bound to the new object, `brand="Toyota"`, `color="Red"`.

**Common mistakes:**
- Calling it "the constructor" loosely — technically `__new__` creates the object and `__init__` initializes it (we cover `__new__` properly in Level 6: Internals). For now, treat `__init__` as "the setup step."
- Forgetting `self.` when assigning — `brand = brand` just creates a local variable that disappears after the method ends; it does **not** attach to the object.

---

## 3. `self` — What It Actually Represents

**Simple explanation:**
`self` is simply **a reference to the specific object the method is currently being called on**. It's not magic — it's just the first parameter Python passes automatically to every instance method.

**Analogy:**
If you have 5 cars and you call `car3.honk()`, `self` inside `honk()` refers to `car3` specifically — not to all cars, not to the class, just to that one object standing in front of you.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print(f"{self.brand} says beep!")

car1 = Car("Toyota")
car2 = Car("Honda")

car1.honk()   # Toyota says beep!
car2.honk()   # Honda says beep!
```

**What's really happening:** `car1.honk()` is secretly translated by Python into `Car.honk(car1)`. `self` is just `car1` under a generic name inside the method body. Try this yourself in the practice file — it makes `self` click immediately.

**Common mistakes:**
- Thinking `self` is a Python keyword — it isn't. You could technically name it anything (`this`, `me`), but every Python developer uses `self` by convention. Don't break the convention.
- Believing `self` refers to the class — it refers to the **instance**, not the class itself.

---

## 4. Instance Attributes vs. Class Attributes

**Simple explanation:**
- **Instance attributes** belong to one specific object — set inside `__init__` via `self.x = ...`. Each object has its own copy.
- **Class attributes** belong to the class itself and are **shared** by every object of that class, unless an object overrides its own copy.

**Analogy:**
"Number of wheels = 4" is true for *every* car — that's a class attribute, defined once. "Color = Red" is specific to *this* car — that's an instance attribute.

```python
class Car:
    wheels = 4                      # class attribute — shared

    def __init__(self, brand):
        self.brand = brand          # instance attribute — per object

car1 = Car("Toyota")
car2 = Car("Honda")

print(car1.wheels, car2.wheels)     # 4 4   (shared)
print(car1.brand, car2.brand)       # Toyota Honda  (independent)

Car.wheels = 6                      # change via the class
print(car1.wheels, car2.wheels)     # 6 6   (both see it)
```

**Common mistakes:**
- Assigning a **mutable** class attribute (like a list) and expecting each object to get its own — they all share the *same* list unless you explicitly create one per instance in `__init__`. This is one of the most common real bugs in Python OOP; we demonstrate it explicitly in the practice file.

---

## 5. Instance Methods, Class Methods, and Static Methods

**Simple explanation:**

| Type | Decorator | First parameter | Operates on |
|---|---|---|---|
| Instance method | *(none)* | `self` | one specific object |
| Class method | `@classmethod` | `cls` | the class itself |
| Static method | `@staticmethod` | *(none)* | neither — just lives inside the class for organization |

```python
class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
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
```

**When to use which:**
- Instance method: default choice — anything that reads/changes one object's state.
- Class method: anything that reads/changes state shared across the whole class, or "alternative constructors" (you'll see this pattern a lot in Level 2+).
- Static method: a utility function that's *logically related* to the class but doesn't need `self` or `cls` at all — it's grouped there for organization only.

**Common mistakes:**
- Making everything a `@staticmethod` "just because it doesn't use `self`" — often it should be a free function outside the class instead, unless it's meaningfully tied to the class's purpose.
- Forgetting `cls.` when a class method should affect all instances, and accidentally shadowing it as a local variable.

---

## 6. Object Creation and Object Identity

**Simple explanation:**
Every object you create is a distinct thing in memory, even if it has identical attribute values to another object. Python gives every object a unique identity you can inspect with `id()`.

```python
car1 = Car("Toyota")
car2 = Car("Toyota")

print(car1 == car2)   # False by default — different objects
print(car1 is car2)   # False — different identity
print(id(car1), id(car2))   # different numbers
```

**Why this matters:** `==` checks *equality* (which you can customize — more in Level 5, Polymorphism), while `is` checks *identity* — "are these literally the same object in memory?" Two cars with identical brand names are still two different cars.

**Common mistakes:**
- Using `is` when you meant `==` (or vice versa). Use `is` only for identity checks (very common pattern: `if x is None`), and `==` for value comparison.

---

## 7. Mutable vs. Immutable Attributes

**Simple explanation:**
Some attribute values can be changed in place (**mutable** — e.g. lists, dicts), others cannot (**immutable** — e.g. strings, integers, tuples). This distinction becomes critical for **default arguments** and **shared class attributes**, where a classic Python trap lives.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand          # str — immutable
        self.features = []          # list — mutable

car1 = Car("Toyota")
car2 = Car("Honda")

car1.features.append("Sunroof")
print(car1.features)   # ['Sunroof']
print(car2.features)   # []   — separate lists, because each __init__ call makes a NEW list
```

Compare this to the class-attribute trap:

```python
class BadCar:
    features = []        # DANGER: defined once, shared by ALL instances

    def __init__(self, brand):
        self.brand = brand

c1 = BadCar("Toyota")
c2 = BadCar("Honda")
c1.features.append("Sunroof")

print(c2.features)   # ['Sunroof']  <-- leaked into c2! Same shared list.
```

**Rule of thumb:** mutable defaults belong inside `__init__` (per-instance), not as bare class attributes — unless you deliberately want sharing.

---

## 8. Basic Encapsulation (preview — full depth in Level 2)

**Simple explanation:**
Encapsulation means bundling data and the methods that operate on it together, and controlling how that data is accessed from outside the object. Python signals intent with naming conventions rather than strict enforcement:

- `self.name` — public, freely accessible.
- `self._name` — "protected" by convention: *please* treat as internal, but Python doesn't stop you.
- `self.__name` — name-mangled: Python renames it internally to make accidental external access harder (not impossible).

```python
class Car:
    def __init__(self, brand):
        self.brand = brand          # public
        self._vin = "HIDDEN123"     # protected by convention
        self.__engine_code = "X9"   # name-mangled

car1 = Car("Toyota")
print(car1.brand)         # fine
print(car1._vin)          # works, but you're not "supposed" to touch it
# print(car1.__engine_code)   # AttributeError!
print(car1._Car__engine_code)  # works — this is what "mangled" means
```

We'll go deep on `@property`, validation, and read-only attributes in Level 2. For now, just recognize the three naming levels and what each *signals* to other developers.

---

## Quick Recap Table

| Concept | One-line meaning |
|---|---|
| Class | Blueprint describing structure and behavior |
| Object | A concrete instance built from a class |
| `__init__` | Runs automatically to set up a new object's initial state |
| `self` | Reference to the specific object a method is running on |
| Instance attribute | Data owned by one object |
| Class attribute | Data shared by every object of that class |
| Instance method | Operates on one object (`self`) |
| Class method | Operates on the class itself (`cls`) |
| Static method | A related utility with no access to `self`/`cls` |
| `id()` | Unique memory identity of an object |
| Mutable vs immutable | Whether an object's value can change in place |
| Encapsulation (basic) | `_protected` / `__mangled` naming signals access intent |

Next up: run `level1_oop_practice.py`, then attempt `level1_oop_exercises.py`.
