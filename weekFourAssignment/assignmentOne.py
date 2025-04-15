import random
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._fuel_level = 100  # Protected attribute

    def drive(self):
        if self._fuel_level <= 0:
            return f"{self.make} {self.model} cannot drive — tank is empty."
        self._fuel_level -= 10
        return f"{self.make} {self.model} is driving. Fuel level: {self._fuel_level}%"

    def refuel(self):
        self._fuel_level = 100
        return f"{self.make} {self.model} has been refueled to {self._fuel_level}%."

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self._fuel_level = random.randint(1, 100)

    def refuel(self):
        self._fuel_level = 100
        return f"{self.make} {self.model} battery charged to {self._fuel_level}%."


class GasCar(Car):
    def __init__(self, make, model, year, tank_capacity):
        super().__init__(make, model, year)
        self.tank_capacity = tank_capacity
        self._fuel_level = random.randint(1, 100)

    def refuel(self):
        self._fuel_level = 100
        return f"{self.make} {self.model} fuel tank filled to {self._fuel_level}%."


# Example usage
if __name__ == "__main__":
    tesla = ElectricCar("Tesla", "Model 3", 2022, battery_capacity=75)
    toyota = GasCar("Toyota", "Corolla", 2018, tank_capacity=50)

    for car in [tesla, toyota]:
        print(car)
        print(car.drive())
        print(car.refuel())
        print()
