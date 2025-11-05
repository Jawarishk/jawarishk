class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance = self.current_speed * hours
        self.distance_traveled += distance


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kWh

    def print_info(self):
        print(f"Electric Car {self.registration_number}:")
        print(f"  Max Speed: {self.max_speed} km/h")
        print(f"  Battery Capacity: {self.battery_capacity} kWh")
        print(f"  Distance Traveled: {self.distance_traveled} km")


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters

    def print_info(self):
        print(f"Gasoline Car {self.registration_number}:")
        print(f"  Max Speed: {self.max_speed} km/h")
        print(f"  Tank Volume: {self.tank_volume} liters")
        print(f"  Distance Traveled: {self.distance_traveled} km")


def main():
    # Create electric car
    electric_car = ElectricCar("ABC-15", 180, 52.5)

    # Create gasoline car
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)


    electric_car.accelerate(120)
    gasoline_car.accelerate(100)

    electric_car.drive(3)
    gasoline_car.drive(3)

    print("After driving for 3 hours:")
    print("-" * 30)
    electric_car.print_info()
    print()
    gasoline_car.print_info()

    print("\n" + "=" * 50)
    print("Additional test with different speeds:")

    electric_car2 = ElectricCar("EV-001", 200, 75.0)
    gasoline_car2 = GasolineCar("PET-456", 180, 45.0)

    electric_car2.accelerate(150)
    gasoline_car2.accelerate(80)

    electric_car2.drive(3)
    gasoline_car2.drive(3)

    print("\nAfter driving for 3 hours (different speeds):")
    print("-" * 40)
    electric_car2.print_info()
    print()
    gasoline_car2.print_info()


if __name__ == "__main__":
    main()