# Base class
class SmartDevice:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self._battery_life = battery_life  # Protected attribute

    def device_info(self):
        return f"{self.brand} {self.model} with {self._battery_life}h battery life"

    def charge(self, hours):
        self._battery_life += hours
        return f"Charged for {hours}h. New battery life: {self._battery_life}h"

# Derived class
class Smartphone(SmartDevice):
    def __init__(self, brand, model, battery_life, os, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.os = os
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        return f"📸 Took a photo with {self.camera_megapixels}MP camera!"

    def device_info(self):  # Method overriding (Polymorphism)
        return (f"{self.brand} {self.model} runs on {self.os}, "
                f"{self._battery_life}h battery, {self.camera_megapixels}MP camera")

# Create instances
device1 = SmartDevice("GenericTech", "AlphaPad", 10)
phone1 = Smartphone("Samsung", "Galaxy S21", 20, "Android", 64)

# Use the methods
print(device1.device_info())
print(device1.charge(2))

print(phone1.device_info())  # Polymorphism in action
print(phone1.take_photo())
print(phone1.charge(1))
