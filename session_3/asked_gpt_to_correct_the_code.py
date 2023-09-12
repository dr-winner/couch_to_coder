# Declaring variables: balance and pin
balance = 10000
pin = 1909

max_attempts = 3  # Set the maximum number of PIN entry attempts

# Loop for PIN entry attempts
for _ in range(max_attempts):
    user_pin = int(input("Please enter your PIN: "))
    
    if user_pin == pin:
        print(f"Welcome! Your current balance is ${balance}")
        
        # Prompt user if they want to withdraw or deposit cash
        print("Would you like to withdraw or deposit?")
        choice = int(input("Select 1. Withdraw 2. Deposit: "))
        
        if choice == 1:  # User chooses to withdraw
            amount = int(input("Please enter the amount you want to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("------Withdrawal successful...------")
                print(f"Your updated balance is ${balance}")
            else:
                print("You have insufficient balance")
        elif choice == 2:  # User chooses to deposit
            amount = int(input("Please enter the amount you want to deposit: "))
            balance += amount
            print("------Deposit successful...------")
            print(f"Your updated balance is ${balance}")
        else:
            print("Invalid choice!")
        
        print("Thank you for transacting with us")
        break  # Exit the loop when the correct PIN is entered
    else:
        print(f"Incorrect PIN! You have {max_attempts - 1} attempt(s) left.")
else:
    print("Access denied! You have exhausted your PIN entry attempts.")
