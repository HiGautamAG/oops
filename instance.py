class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Create an instance of the class
my_dog = Dog(name="Buddy", breed="Golden Retriever")

# Use the instance
print(my_dog.bark())  # Output: Buddy says woof!
