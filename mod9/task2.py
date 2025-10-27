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
        # Ensure speed doesn't go below zero
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed


def main():

    new_car = Car("ABC-123", 142)

    print("Initial speed:", new_car.current_speed, "km/h")

    new_car.accelerate(30)
    print("After +30 km/h:", new_car.current_speed, "km/h")

    new_car.accelerate(70)
    print("After +70 km/h:", new_car.current_speed, "km/h")

    new_car.accelerate(50)
    print("After +50 km/h:", new_car.current_speed, "km/h")

    new_car.accelerate(-200)
    print("After emergency brake (-200 km/h):", new_car.current_speed, "km/h")

if __name__ == "__main__":
    main()