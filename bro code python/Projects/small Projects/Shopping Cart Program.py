#Shoping cart Program

foods =[]
prices = []
total = 0


while True :
    food = input("Enter Your item (q to quit): ")
    if food.lower() == "q":
     break
    else:
       price = input(f"Enter the price of {food}:$")
       foods.append(food)
       prices.append(float(price))


print("----- Your Cart -----")


for food in foods:
   print(food, end=" ")

for price in prices:
   total += price

print( )  
print(f"Your total is {total}$")