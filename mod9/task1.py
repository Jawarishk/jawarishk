class Car:
    def __init__(self, registration_no, max_speed):
        self.registration_no = registration_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

def main():
    new_car = Car("ABC-123", 142)
    print(f"Registration Number: {new_car.registration_no}")
    print(f"Maximum Speed: {new_car.max_speed} km/h")
    print(f"Current Speed: {new_car.current_speed} km/h")
    print(f"Travelled Distance: {new_car.travelled_distance} km")

if __name__ == "__main__":
    main()