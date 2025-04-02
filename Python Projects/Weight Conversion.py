# Weight converting code

weight = float(input("Please enter your weight: "))
unit = input("Kilograms or Pounds? (K/P) ")

if unit == "K" :
    weight = weight *2.205
    unit = "Lbs"
    print(f"Your weight is: {weight} {unit}")


elif unit =="P":
    weight = weight / 2.205
    unit = "kgs."
    print(f"Your weight is: {weight} {unit}")

else:
    print(f"{weight} {unit} is not valid! ")



