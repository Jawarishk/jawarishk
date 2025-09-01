length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42

if length >= size_limit:
    print("You can keep the zander!")
else:
    below_limit = size_limit - length
    print(f"Release the fish back into the lake.")
    print(f"The zander is {below_limit:.1f} cm below the size limit.")