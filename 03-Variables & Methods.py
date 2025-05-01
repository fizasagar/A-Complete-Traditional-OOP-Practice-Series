class Car:
    def __init__(self, brand):
        # public variable
        self.brand = brand

    # public method
    def start(self):
        print(f"{self.brand} car is starting...")

# Creating an object
my_car = Car("Toyota")

# Accessing public variable
print("Brand:", my_car.brand)

# Calling public method
my_car.start()
