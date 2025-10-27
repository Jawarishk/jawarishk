class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range!")
            return

        if target_floor > self.current_floor:
            while self.current_floor < target_floor:
                self.floor_up()
        elif target_floor < self.current_floor:
            while self.current_floor > target_floor:
                self.floor_down()
        else:
            print(f"Already on floor {target_floor}")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")
        else:
            print("Already at top floor!")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")
        else:
            print("Already at bottom floor!")


def main():
    elevator = Elevator(1, 10)

    print("Moving to floor 5:")
    elevator.go_to_floor(5)

    print("\nMoving back to bottom floor:")
    elevator.go_to_floor(1)


if __name__ == "__main__":
    main()