# calculator

opertor = input("Enter an opertor( +,-,*,/,% ): ")

num1 = float(input("Enter the first num: "))
num2 = float(input("Enter the second num: "))

if opertor == "+":
    print(f"Result - {num1 + num2}")

elif opertor == "-":
    print(f"Result - {num1 - num2}")

elif opertor == "*":
    print(f"Result - {num1 * num2}")

elif opertor == "/":
    print(f"Result - {num1 / num2}")

elif opertor == "%":
    print(f"Result - {num1 % num2}")
else:
    print(f"{opertor} Not a valid opertor...!")