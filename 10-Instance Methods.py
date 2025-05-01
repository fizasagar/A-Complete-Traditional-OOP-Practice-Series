class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name}, the {self.breed}, is barking! 🐾")

# Create object
dog1 = Dog("Bruno", "Labrador")
dog1.bark()
