class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving..."

# Subclasses demonstrating polymorphism
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on water 🚤"

# Create instances
vehicles = [
    Car("Toyota"),
    Plane("Boeing 747"),
    Boat("Yamaha Speedboat")
]

# Test polymorphic behavior
for vehicle in vehicles:
    print(vehicle.move())
