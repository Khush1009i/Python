# Movie Booking System with Food Ordering and Bill Generation

def generate_bill(name, movie_name, seat_name, seat_price, seat_quantity, food_orders, tip):
    total_seat_price = seat_price * seat_quantity
    total_food_price = sum(food_orders.values())
    total_price = total_seat_price + total_food_price + tip

    print("\n" + "="*30)
    print(f"         FINAL BILL")
    print("="*30)
    print(f"Name        : {name}")
    print(f"Movie       : {movie_name}")
    print(f"Seat Type   : {seat_name}")
    print(f"Seat Price  : ₹{seat_price} x {seat_quantity} = ₹{total_seat_price}")
    print("-"*30)
    
    if food_orders:
        print("Food Orders:")
        for item, price in food_orders.items():
            print(f"  - {item}: ₹{price}")
    else:
        print("Food Orders : None")

    print("-"*30)
    print(f"Staff Tip   : ₹{tip}")
    print("="*30)
    print(f"Total Price : ₹{total_price}")
    print("="*30)
    print("\nThank you for your visit! Enjoy your movie! 🍿🎬\n")


def seats(name, quantity, movie_name):
    print("\n**** Type of Seats **** ")
    print("1.  Classic          : ₹180  ")
    print("2.  Prime            : ₹250  ")
    print("3.  Recliner         : ₹450  ")
    print("4.  Gold Class       : ₹600  ")
    print("\nE to exit\n")

    while True:  
        choose = input("Enter your choice: ").strip().lower()

        if choose == "e":  
            print("Thanks for the visit!") 
            return None, None, None  # Exit the function

        if choose in ["1", "2", "3", "4"]:
            seat_types = {
                "1": ("Classic", 180),
                "2": ("Prime", 250),
                "3": ("Recliner", 450),
                "4": ("Gold Class", 600),
            }

            seat_name, price = seat_types[choose]
            print(f"\n{name}, you have booked {quantity} {seat_name} seat(s) for ₹{price * quantity}, for '{movie_name}'.")
            print("Enjoy your movie!\n")

            # Call food ordering function
            food_orders = food_to_order(name)

            # Ask for tip
            tip = input("\nWould you like to give a tip for the staff? (₹ Amount or N for no tip): ").strip()
            tip_amount = int(tip) if tip.isdigit() else 0

            # Generate final bill
            generate_bill(name, movie_name, seat_name, price, quantity, food_orders, tip_amount)

            return seat_name, price, quantity

        else:
            print("Invalid choice! Please select a valid option.\n")


def movie_booking():
    print("\n****** Movie Menu ******")
    print("     Movies             : Lang available  ")
    print("1.  Interstellar        : English  ")
    print("2.  The Prestige        : English ")
    print("3.  Fight Club          : English  ")
    print("4.  Inception           : English ")
    print("5.  Mickey 17           : English ")
    print("6.  Bangalore Days      : Kannada  ")
    print("7.  Premam              : Telugu  ")
    print("8.  Gulaal              : Hindi  ")
    print("9.  QAARWAAN            : Hindi  ")
    print("10. Om-Dar-B-Dar        : Hindi  ")
    print("\nE to exit\n")

    while True:  
        option_choose = input("Enter your choice: ").strip().lower()

        if option_choose == "e":  
            print("Thanks for the visit!") 
            return  # Exit the function

        if option_choose in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            name = input("Enter your name: ").strip()
            quantity = int(input("How many tickets do you want? "))

            movies = {
                "1": ("Interstellar", "English"),
                "2": ("The Prestige", "English"),
                "3": ("Fight Club", "English"),
                "4": ("Inception", "English"),
                "5": ("Mickey 17", "English"),
                "6": ("Bangalore Days", "Kannada"),
                "7": ("Premam", "Telugu"),
                "8": ("Gulaal", "Hindi"),
                "9": ("QAARWAAN", "Hindi"),
                "10": ("Om-Dar-B-Dar", "Hindi")
            }

            movie_name, language = movies[option_choose]

            print(f"\n{name}, you have booked {quantity} ticket(s) for '{movie_name}' with '{language}' dub.\n")
            
            # Call seats function to select seat type and finalize booking
            seats(name, quantity, movie_name)
            return  # Exit after seat selection

        else:
            print("Invalid choice! Please select a valid option.\n")


def food_to_order(name):
    food_orders = {}

    quest = input(f"{name}, would you like to order anything to eat? (Y/N): ").strip().lower()

    if quest == "y":  
        print("\n****** Food Menu ******")
        print("1. Normal Popcorn       : ₹50  ")
        print("2. Butter Popcorn       : ₹100 ")
        print("3. Sandwich             : ₹60  ")
        print("4. Grilled Sandwich     : ₹130 ")
        print("5. Extra Cheese Sandwich: ₹150 ")
        print("6. Coca-Cola            : ₹50  ")
        print("7. Pepsi                : ₹50  ")
        print("E to exit\n")

        while True:  
            food = input("Enter your choice: ").strip().lower()

            if food == "e":  
                print(f"Thanks for ordering, {name}! Enjoy your movie and snacks!") 
                return food_orders  # Exit with food orders

            if food in ["1", "2", "3", "4", "5", "6", "7"]:
                quantity = int(input("How much do you want? "))
                items = {
                    "1": ("Normal Popcorn", 50),
                    "2": ("Butter Popcorn", 100),
                    "3": ("Sandwich", 60),
                    "4": ("Grilled Sandwich", 130),
                    "5": ("Extra Cheese Sandwich", 150),
                    "6": ("Coca-Cola", 50),
                    "7": ("Pepsi", 50)
                }
                item_name, price = items[food]
                food_orders[item_name] = price * quantity
                print(f"You have ordered {quantity} {item_name}(s) for ₹{price * quantity}.")

            else:
                print("Invalid choice! Please select a valid option.")

    else:
        print(f"Alright {name}, no snacks! Enjoy your movie! 🍿🎬")
        return food_orders


# Call movie booking function
movie_booking()
