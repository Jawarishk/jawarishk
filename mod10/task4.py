import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def drive(self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Registration':<15} {'Max Speed':<12} {'Current Speed':<15} {'Distance':<12}")
        print("-" * 60)
        for car in self.cars:
            print(
                f"{car.registration_number:<15} {car.max_speed:<12} {car.current_speed:<15} {car.travelled_distance:<12.2f}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration_number, max_speed)
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)

    print(f"Race: {race.name}")
    print(f"Distance: {race.distance} km")
    print("Race started!\n")

    hour = 0
    while not race.race_finished():
        hour += 1
        race.hour_passes()

        if hour % 10 == 0:
            print(f"\n=== After {hour} hours ===")
            race.print_status()

    print(f"\n=== RACE FINISHED after {hour} hours! ===")
    race.print_status()

    winner = max(race.cars, key=lambda car: car.travelled_distance)
    print(f"\nWINNER: {winner.registration_number} with {winner.travelled_distance:.2f} km!")


if __name__ == "__main__":
    main()