def main():
    airports = {}

    while True:
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            icao = input("Enter the ICAO code: ").strip().upper()
            name = input("Enter the airport name: ").strip()
            airports[icao] = name
        elif choice == "2":
            icao = input("Enter the ICAO code: ").strip().upper()
            if icao in airports:
                print(airports[icao])
            else:
                print("Not found")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
