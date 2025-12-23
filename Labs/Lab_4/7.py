class Transport:
    def __init__(self, name):
        self.name = name
    def maxSpeed(self):
        pass
    def fuelConsumption(self):
        pass

class Car(Transport):
    def maxSpeed(self):
        return 180
    def fuelConsumption(self):
        return 8

class Bicycle(Transport):
    def maxSpeed(self):
        return 25
    def fuelConsumption(self):
        return 0

class Bus(Transport):
    def maxSpeed(self):
        return 120
    def fuelConsumption(self):
        return 20
    
car = Car("Toyota")
print(f"Car {car.name}:")
print(f" Макс. скорость: {car.maxSpeed()}")
print(f" Расход: {car.fuelConsumption()} л/100км")

bicycle = Bicycle("Stels")
print(f"Bicycle {bicycle.name}:")
print(f" Макс. скорость: {bicycle.maxSpeed()}")
print(f" Расход: {bicycle.fuelConsumption()}")

bus = Bus("ЛиАЗ")
print(f"Bus {bus.name}:")
print(f" Макс. скорость: {bus.maxSpeed()}")
print(f" Расход: {bus.fuelConsumption()} л/100км")