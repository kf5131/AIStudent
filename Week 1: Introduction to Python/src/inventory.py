# Base class Vehicle
class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price


class Car(Vehicle):
    def __init__(self, make, model, year, price, num_doors):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price} (Car, {self.num_doors} doors)"

class Truck(Vehicle):
    def __init__(self, make, model, year, price, cargo_capacity):
        super().__init__(make, model, year, price)
        self.cargo_capacity = cargo_capacity

    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price} (Truck, Payload capacity: {self.cargo_capacity} kg)"


# Inventory list
inventory = [
    Car("Toyota", "Corolla", 2020, 24000, 4),
    Truck("Ford", "F-150", 2021, 35000, 10000),
    Car("Honda", "Civic", 2022, 22000, 4)
]

# Display all vehicles and calculate total value
total_value = 0
for vehicle in inventory:
    print(vehicle)
    total_value += vehicle.price

print(f"Total inventory value: ${total_value}")