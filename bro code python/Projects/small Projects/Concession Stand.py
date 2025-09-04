# Concession stand program using dictionary : 


menu = {
    "pizza": 100,
    "burger": 100,
    "dessert": 70,
    "lemonade": 100,
    "ice-Cream": 170,
    "frenchfries": 70
}

cart = []
total = 0

print("----------  MENU  ----------")
for key, value in menu.items():
    print(f"{key:10} : {value: .2f}₹")
print("------------------------------")

while True:
    food = input("Select an Item (q to quit): ")
    if food.lower() == "q":
        break
    elif food in menu:  # Check if the food is in the menu
        cart.append(food)
    else:
        print("Sorry, that item is not on the menu. Please choose again.")

# Calculate total and print cart items if cart is not empty
if cart:
    print("Items in your cart: ", end="")
    for food in cart:
        total += menu[food]  # Calculate total based on the cart items
        print(food, end=" ")

    print(" ")
    print(f"Total is: {total:.2f}₹")  # Display the total amount
else:
    print("No items selected.")

print("------------------------------")
