weight = float(input("Enter weight: "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K":
    weight * 2.205
    unit = "Lbs."
    print(f"Weight is: {round(weight, 1)}{unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Weight is: {round(weight, 1)}{unit}")
else:
    print(f"{unit} is not a valid character.")