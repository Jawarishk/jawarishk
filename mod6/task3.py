def gallons_to_litres(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter gasoline in gallons (negative value to quit): "))
        if gallons < 0:
            print("Goodbye!")
            break
        litres = gallons_to_litres(gallons)
        print(f"{gallons} gallons is {litres:.2f} litres")

main()
