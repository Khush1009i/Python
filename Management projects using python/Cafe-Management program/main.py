# Cafe Management Program

def main():
    order_summary = []  # Stores the user's order
    total_amount = 0  # Stores the total price
    
    name = input("\nEnter your name: ")  # Ask for name only once
    
    while True:
        print("\n****** Welcome to the Cafe ******")
        print("What would you like to drink?")
        print("1. Tea")            
        print("2. Coffee")
        print("3. Cold drink")
        print("4. Water")
        print("5. Exit & Generate Bill")
        print()

        choice = input("Enter your choice (1 - 5): ")

        if choice == '1':
            item, price = tea(name)  
        elif choice == '2':
            item, price = coffee(name)
        elif choice == '3':
            item, price = cold_drink(name)
        elif choice == '4':
            print("💧 Water has been served for free!")
            item, price = "Water", 0
        elif choice == '5':
            print("\nGenerating Bill...")
            generate_bill(order_summary, total_amount, name)
            break  # Exit the loop
        else:
            print("Invalid request! Please enter a valid option.")
            continue
        
        # Add to order summary if an item was ordered
        if item:
            order_summary.append((item, price))
            total_amount += price

# Tea Section
def tea(name):
    while True:
        print("\n****** TYPES OF TEA ******")
        print("1. Normal Tea (₹20)")
        print("2. Black Tea (₹50)")
        print("3. Green Tea (₹50)")
        print("4. Go back to Main Menu")
        print()

        typetea = input("Enter the type of tea you want: ")

        if typetea == '1':
            print(f"Normal Tea has been placed for {name}.")
            return "Normal Tea", 20
        elif typetea == '2':
            print(f"Black Tea has been placed for {name}.")
            return "Black Tea", 50
        elif typetea == '3':
            print(f"Green Tea has been placed for {name}.")
            return "Green Tea", 50
        elif typetea == '4':
            return None, 0  # Return to main menu
        else:
            print("Invalid choice. Try again!")

# Coffee Section
def coffee(name):
    while True:
        print("\n****** TYPES OF COFFEE ******")
        print("1. Normal Coffee (₹20)")
        print("2. Black Coffee (₹50)")
        print("3. Cold Coffee (₹100)")
        print("4. Go back to Main Menu")
        print()

        typecoffee = input("Enter the type of coffee you want: ")

        if typecoffee == '1':
            print(f" Normal Coffee has been placed for {name}.")
            return "Normal Coffee", 20
        elif typecoffee == '2':
            print(f" Black Coffee has been placed for {name}.")
            return "Black Coffee", 50
        elif typecoffee == '3':
            print(f" Cold Coffee has been placed for {name}.")
            return "Cold Coffee", 100
        elif typecoffee == '4':
            return None, 0  # Return to main menu
        else:
            print(" Invalid choice. Try again!")

# Cold Drink Section
def cold_drink(name):
    while True:
        print("\n****** TYPES OF COLD DRINKS ******")
        print("1. Coca Cola (₹40)")
        print("2. Pepsi (₹40)")
        print("3. Sprite (₹40)")
        print("4. Mountain Dew (₹50)")
        print("5. Fanta/Slice (₹50)")
        print("6. Go back to Main Menu")
        print()

        colddrink = input("Enter the cold drink you want: ")

        if colddrink == '1':
            print(f" Coca Cola has been placed for {name}.")
            return "Coca Cola", 40
        elif colddrink == '2':
            print(f" Pepsi has been placed for {name}.")
            return "Pepsi", 40
        elif colddrink == '3':
            print(f" Sprite has been placed for {name}.")
            return "Sprite", 40
        elif colddrink == '4':
            print(f" Mountain Dew has been placed for {name}.")
            return "Mountain Dew", 50
        elif colddrink == '5':
            print(f" Fanta/Slice has been placed for {name}.")
            return "Fanta/Slice", 50
        elif colddrink == '6':
            return None, 0  # Return to main menu
        else:
            print(" Invalid choice. Try again!")

# Generate Bill
def generate_bill(order_summary, total_amount, name):
    print("\n********** Final Bill **********")
    print(f"Customer Name: {name}")
    print("\nItems Ordered:")
    if not order_summary:
        print("No items were ordered.")
    else:
        for item, price in order_summary:
            print(f"- {item} - ₹{price}")
        
        print("\nTotal Amount: ₹", total_amount)    
    print("\nThank you for visiting! Have a great day. 😊\n")

main()
