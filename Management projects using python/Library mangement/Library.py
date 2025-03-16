# library mangement system in python:

# for Registration for new student:
def registration():
    name = input("Enter your name: ")
    college_id = int(input("Enter your college id: "))
    age = int(input("Enter your age: "))

    Year = int(input("Enter your year: ")) 

    if Year == 1:
        print("You can issue one book at a time")    
        print("A book is allowed till 15 days only.")
        print("You can re-issue the book from the Librarian.")
    elif Year == 2 or Year == 3:
        print("You can issue 2 books at a time")
        print("A book is allowed till 15 days only.")
        print("You can re-issue the book from the Librarian.")
    elif Year == 4:
        print("You can issue 2 books at a time")
        print("A book is allowed till 15 days only.")
        print("You can re-issue the book from the Librarian, after 15 days") 
    else:
        print("NOT A VALID YEAR  ...!")

# To issue book :
def issue_book():
    name = input("Enter your name: ")
    college_id = int(input("Enter your college id: "))

    num_of_book = int(input("Number of books you want to issue: "))
    if num_of_book == 1:
        name_of_book1 = input("Enter the name of the book: ")
        print("You have issued:", name_of_book1.capitalize())
        print("Submit or Re-issue books within 15 days")
        print("WARNING : Penalty will be of 60₹/day")

    elif num_of_book == 2:
        name_of_book1 = input("Enter the name of the first book: ")
        name_of_book2 = input("Enter the name of the second book: ")
        print("You have issued:", name_of_book1.capitalize(), "&", name_of_book2.capitalize())
        print("Submit or Re-issue books within 15 days")
        print("WARNING : Penalty will be of 60₹/day")

    else:
        print("You can issue only 1 or 2 books.")
        print()
        return issue_book()
    
    from datetime import datetime, timedelta
    
    date_of_issue = input("Enter the date of issue (DD/MM/YYYY): ")
    issue_date = datetime.strptime(date_of_issue, "%d/%m/%Y")
    return_date = issue_date + timedelta(days=15)
    
    print("Date of Issue:", issue_date.strftime("%d-%m-%Y"))
    print("Submit (Return) Date:", return_date.strftime("%d-%m-%Y"))



    
 

def return_book():
    name = input("Enter your name: ")
    college_id = int(input("Enter your college id: "))

    num_of_book = int(input("Number of books you want to returning: "))
    if num_of_book == 1:
        name_of_book1 = input("Enter the name of the book: ")
        print("You are returning:", name_of_book1.capitalize())

    elif num_of_book == 2:
        name_of_book1 = input("Enter the name of the first book: ")
        name_of_book2 = input("Enter the name of the second book: ")
        print("You are returning:", name_of_book1.capitalize(), "&", name_of_book2.capitalize())

    else:
        print("INVALID REQUEST...!!!")
        print()
        return return_book()


def main():
    is_running = True

    while is_running:
        print("\n************ Library Management System ************")
        print("1. New Registration")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")
        print()

        choice = input("Enter your choice (1 - 4): ")

        if choice == '1':
            registration()  # New student registration
        elif choice == '2': 
            issue_book()    # Issue a book
        elif choice == '3': 
            return_book()   # Return a book
        elif choice == '4': 
            is_running = False
            print("Thank you! Have a nice day.")
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
