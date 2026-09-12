# Day 22: Inheritance & Polymorphism

# 1. Basic Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()
cat.speak()

# 2. Using super()
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        print(f"{self.year} {self.brand}")

class ElectricCar(Vehicle):
    def __init__(self, brand, year, battery_range):
        super().__init__(brand, year)
        self.battery_range = battery_range
    
    def info(self):
        super().info()
        print(f"Battery Range: {self.battery_range} km")

tesla = ElectricCar("Tesla", 2023, 500)
tesla.info()

# 3. Polymorphism
class AIModel:
    def __init__(self, name):
        self.name = name
    
    def predict(self, data):
        return "Base prediction"

class TextModel(AIModel):
    def predict(self, data):
        return f"Text analysis: '{data}'"

class ImageModel(AIModel):
    def predict(self, data):
        return f"Image analysis: '{data}'"

models = [TextModel("GPT"), ImageModel("DALL-E")]
for model in models:
    print(f"{model.name}: {model.predict('sample')}")