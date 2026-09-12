# Day 21: Classes & Objects (OOP)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

# Create cars
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model 3", 2023)

car1.display_info()
car2.display_info()

# Bank Account class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

acc = BankAccount("Athul", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(5000)

# Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Athul", [95, 88, 92])
print(f"{s1.name}'s average: {s1.average():.2f}")