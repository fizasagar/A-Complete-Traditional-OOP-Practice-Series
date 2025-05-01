class Engine:
    def start_engine(self):
        """Method to start the engine."""
        return "Engine started!"

class Car:
    def __init__(self, engine):
        """Car class has an Engine object passed during initialization."""
        self.engine = engine

    def start_car(self):
        """Method to start the car using the engine's start_engine method."""
        return self.engine.start_engine()

# Create an Engine object
car_engine = Engine()

# Pass the Engine object to the Car object during initialization
my_car = Car(car_engine)

# Access the start_engine method via the Car class
print(my_car.start_car())
