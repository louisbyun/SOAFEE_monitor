
class Vehicle:
    def __init__(self, fuel_level, speed):
        self.fuel_level = fuel_level
        self.speed = speed

    def check_fuel(self):
        if self.fuel_level < 10:
            print("Warning: Low fuel level.")
        else:
            print("Fuel level is sufficient.")

    def check_speed(self):
        if self.speed > 120:
            print("Warning: Speeding!")
        elif self.speed < 10:
            print("Warning: Driving too slow.")
        else:
            print("Speed is within normal range.")

# Create a vehicle instance and check its status
my_vehicle = Vehicle(fuel_level=5, speed=130)
my_vehicle.check_fuel()
my_vehicle.check_speed()
