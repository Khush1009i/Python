# A compound  interest calculator:

principle = 0
rate = 0
time = 0

while  True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to 0")
    else:
        break

while  True:
    rate = float(input("Enter the rate interest: "))
    if rate <0:
        print("Principle can't be less than or equal to 0")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <0:
        print("Principle can't be less than or equal to 0")
    else:
        break


print(f"Your principle amount is {principle}$")
print(f"Your interest rate  is {rate}%")
print(f"Your time  {time} years")

# Total 
Total = principle * pow( (1+ rate/100), time)
print(f"Balance after {time} year /s:{Total:.2f}$")