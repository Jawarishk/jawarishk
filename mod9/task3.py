class Car:
    def __init__(self, registration_no, max_speed):
        self.registration_no = registration_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):

        new_speed = self.current_speed + speed_change

        if new_speed > self.max_speed:
            self.current_speed = self.max_speed

        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):

        distance_traveled = self.current_speed * hours

        self.travelled_distance += distance_traveled


def main():

    car = Car("ABC-123", 142)

    car.current_speed = 60
    car.travelled_distance = 2000

    print(f"Before driving:")
    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance} km")

    car.drive(1.5)

    print(f"\nAfter driving 1.5 hours at {car.current_speed} km/h:")
    print(f"Travelled distance: {car.travelled_distance} km")

    car.drive(2)
    print(f"\nAfter driving 2 more hours:")
    print(f"Travelled distance: {car.travelled_distance} km")


if __name__ == "__main__":
    main()