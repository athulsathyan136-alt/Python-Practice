# Day 23: Magic Methods (Dunder Methods)

print("=" * 40)
print("1. __str__ (Print-friendly)")
print("=" * 40)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

book = Book("Python Guide", "Athul", 300)
print(book)

print("\n" + "=" * 40)
print("2. __len__ (len() function)")
print("=" * 40)

class BookWithLen:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages

book2 = BookWithLen("AI Handbook", 450)
print(f"Pages in book: {len(book2)}")

print("\n" + "=" * 40)
print("3. __add__ (Adding objects)")
print("=" * 40)

class Wallet:
    def __init__(self, amount):
        self.amount = amount
    
    def __add__(self, other):
        return Wallet(self.amount + other.amount)
    
    def __str__(self):
        return f"Wallet(${self.amount})"

w1 = Wallet(100)
w2 = Wallet(250)
w3 = w1 + w2
print(f"{w1} + {w2} = {w3}")

print("\n" + "=" * 40)
print("4. __eq__ (Comparing objects)")
print("=" * 40)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(2, 3)
p3 = Point(5, 7)

print(f"{p1} == {p2} ? {p1 == p2}")
print(f"{p1} == {p3} ? {p1 == p3}")

print("\n" + "=" * 40)
print("5. __call__ (Making object callable)")
print("=" * 40)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(f"double(5) = {double(5)}")
print(f"triple(5) = {triple(5)}")