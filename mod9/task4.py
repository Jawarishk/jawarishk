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


def main():
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        car = Car(registration_number, max_speed)
        cars.append(car)

    print("Race started! 10 cars are competing.")
    print("First car to reach 10,000 km wins!\n")

    hour = 0
    race_finished = False

    while not race_finished:
        hour += 1
        print(f"Hour {hour}:")

        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_finished = True
                print(f"\n{car.registration_number} has reached 10,000 km! Race finished after {hour} hours.")
                break

    print("\n" + "=" * 60)
    print("FINAL RACE RESULTS")
    print("=" * 60)
    print(f"{'Registration':<15} {'Max Speed':<12} {'Final Speed':<12} {'Distance':<12}")
    print("-" * 60)

    for car in cars:
        print(
            f"{car.registration_number:<15} {car.max_speed:<12} {car.current_speed:<12} {car.travelled_distance:<12.2f}")

    winner = max(cars, key=lambda car: car.travelled_distance)
    print(f"\nWINNER: {winner.registration_number} with {winner.travelled_distance:.2f} km!")

if __name__ == "__main__":
    main()