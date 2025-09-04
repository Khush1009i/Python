def show_balance(balance):
    print("*************************")
    print(f"Your balance: {balance: .2f}$")
    print("*************************")   

def deposit(balance):
    amount = float(input("Enter amount you want to deposit: "))
    if amount <= 0:
        print("Enter a valid amount")
        return balance  # No change if invalid deposit amount
    else:
        balance += amount
        print(f"Deposited: {amount}$")
        return balance

def withdraw(balance):
    amount = float(input("Enter amount you want to withdraw: "))
    if amount <= 0:
        print("Enter a valid amount to withdraw.")
        return balance  # No change if invalid withdraw amount
    elif amount > balance:
        print("Insufficient balance.")
        return balance
    elif amount > 1000:
        print("Cannot withdraw more than 1000$ at a time.")
        return balance
    else:
        balance -= amount
        print(f"Withdrew: {amount}$")
        return balance

def new_account():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Determine account type based on age
    if age <= 18:
        account_type = "Child account"
        balance = 1000  # default balance
    elif 18 < age <= 50:
        account_type = "Adult account"
        balance = 2000  # default balance
    else:  # age > 50
        account_type = "Old account"
        balance = 1000  # default balance
    
    address = input("Enter your residential address: ")
    gender = input("Enter your gender: ")
    adhar_card = input("Enter your Aadhar card number: ")  # Assuming you want this input
    account_num = 123456789  # Placeholder for account number, you can generate or ask for it.

    # Store account details in a dictionary
    account_details = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Address": address,
        "Account Type": account_type,
        "Balance": balance,
        "Aadhar Card Number": adhar_card,
        "Account Number": account_num
    }

    # Print all details at once
    print("\nAccount Details:")
    for key, value in account_details.items():
        print(f"{key}: {value}")

    return account_details, balance  # Return both account details and the balance

def main():
    is_running = True
    account_details = None
    balance = 0  # Initialize balance to 0 initially

    while is_running:
        print("\nBanking Program")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Create New Account")
        print("5. Exit")
        print()

        if account_details is None:  # No account is created yet
            print("Please create an account to proceed.")
            choice = input("Enter your choice (1 - 5): ")

        else:  
            choice = input("Enter your choice (1 - 5): ")

        if choice == '1':
            if account_details:  # Ensure an account has been created
                show_balance(account_details["Balance"])
            else:
                print("No account found. Please create an account first.")

        elif choice == '2':
            if account_details:  # Ensure an account has been created
                balance = deposit(balance)
            else:
                print("No account found. Please create an account first.")

        elif choice == '3':
            if account_details:  # Ensure an account has been created
                balance = withdraw(balance)
            else:
                print("No account found. Please create an account first.")

        elif choice == '4':
            account_details, balance = new_account()  # Create new account and get balance

        elif choice == '5':
            is_running = False
            print("Thank you! Have a nice day.")

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
