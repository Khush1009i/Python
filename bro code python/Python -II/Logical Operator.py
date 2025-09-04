# logical operator = evaluate multiple conditiond(or, not, and)
# or  - atleast condtions one true
# and - both condtions must be true
# not - inverts the condtions


temp = int(input("Enter the tempertaure of outdoor: "))
is_raining = True
is_sunny = True

# using "or":
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The event is on!")


if temp>= 28 and is_raining:
    print("It's Hot outside")
    print("It's Sunny")
elif 0< temp < 28 and not is_sunny:
    print("It's Hot outside")
    print("It's cloudy")

elif temp <= 0 and is_sunny:
    print("Its cold outside")
    print("It's Sunny")

elif 0< temp <28  and is_sunny:
    print("It's warm outside!")
    print("It's Sunny")
elif 0< temp <28  and  not is_sunny:
    print("It's warm outside!")
    print("It's cloudy!")