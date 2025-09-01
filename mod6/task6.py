import math

def unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)
    return price_eur / area_m2

def main():
    print("Pizza 1:")
    d1 = float(input("Enter diameter (cm): "))
    p1 = float(input("Enter price (€): "))
    print("Pizza 2:")
    d2 = float(input("Enter diameter (cm): "))
    p2 = float(input("Enter price (€): "))

    unit1 = unit_price(d1, p1)
    unit2 = unit_price(d2, p2)

    print(f"Pizza 1 unit price: {unit1:.2f} €/m²")
    print(f"Pizza 2 unit price: {unit2:.2f} €/m²")

    if unit1 < unit2:
        print("Pizza 1 provides better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")

main()
