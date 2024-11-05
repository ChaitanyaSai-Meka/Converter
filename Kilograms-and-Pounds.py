weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "P":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} is not valid.")

print(f"Your weight is: {weight} {unit}")
