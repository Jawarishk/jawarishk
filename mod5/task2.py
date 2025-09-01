numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")

# Sort the numbers in descending order and get the top 5
numbers.sort(reverse=True)
top_five = numbers[:5]

print("\nThe five greatest numbers in descending order:")
for num in top_five:
    print(num)