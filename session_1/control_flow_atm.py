# Declaring variables, balance and pin
balance = 10000
pin = 1909

# Greetings
print("Hello our cherished customer!")
# Prompt user for pin input and allow access if correct, else deny

while( number_)
user_pin = int(input("Please enter your pin: ")) # Take input as an integer
if user_pin == pin:
    # Display user's cash balance
    print(f"Welcome! Your current balance is ${balance}")
else:
    # Deny access if input pin is incorrect
    print("Incorrect pin, Access denied!")
    # Prompt user if they want to withdraw or deposit cash
if user_pin == pin:
    print("Would you like to withdraw or deposit?")
    # User choose to withdraw or deposit cash
    choice = int(input("Select 1. Withdraw 2. Deposit: ")) # Take input as an integer
    if choice == 1: # User chooses to withdraw
        # Prompt user to enter the amount to withdraw
        amount = int(input("Please the amount you want to withdraw: ")) # Take input as an integer
        if amount <= balance: # If amount to withdraw is not more than balance
            balance -= amount # Balance = balance - amount
            print("------Withdrawal successful...------")
            print(f"Your updated balance is ${balance}")
        elif choice >= amount: # If the amount is more than balance
            print("You have insufficient balance")
        else:
            print("Invalid amount!") # If input amount is invalid
            # If the user chooses to deposit
    elif choice == 2:
        amount = int(input("Please enter the amount you want to deposit: ")) # Take input as an integer
        balance += amount # balance = balance + amount
        # Successful deposit
        print("------Deposit successfully...------")
        print(f"Your updated balance is ${balance}")
    else:
        # If the user enters invalid choice
        print("Invalid choice!")
print("Thank you for tansacting with us")