# 1. Vector კლასი

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(3, 4)
v3 = v1 + v2

print(v1)  # (2, 3)
print(v2)  # (3, 4)
print(v3)  # (5, 7)


# 2. Book კლასი

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.title == other.title and self.author == other.author


book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Brave New World", "Aldous Huxley")

print(book1 == book2)  # True
print(book1 == book3)  # False


# 3. Car კლასი

class Car:
    def __new__(cls, brand, model, year):
        # __new__ ქმნის ობიექტს
        return super().__new__(cls)

    def __init__(self, brand, model, year):
        # __init__ ანიჭებს ობიექტს საწყის მნიშვნელობებს
        self.brand = brand
        self.model = model
        self.year = year

    # brand getter და setter
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Brand must be a non-empty string.")

        self._brand = value.strip()

    # model getter და setter
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Model must be a non-empty string.")

        self._model = value.strip()

    # year getter და setter
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("Year must be an integer.")

        if value < 1886:
            raise ValueError("Year must be 1886 or later.")

        self._year = value


car = Car("Toyota", "Camry", 2020)

print(car.brand)  # Toyota
print(car.model)  # Camry
print(car.year)   # 2020


car.brand = "BMW"
car.model = "X5"
car.year = 2024

print(car.brand)  # BMW
print(car.model)  # X5
print(car.year)   # 2024