gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid gender input. Please enter 'male' or 'female'.")