# Declaring variables, balance and pin
balance = 10000
pin = 1909
user_pin = 0
number_of_tries = 3

# if(not user_pin.isdigit()):
# Loop for the PIN entry attempts
print("Hello our cherished customer!")
while(number_of_tries > 0):


    # Prompt user for pin input and allow access if correct, else deny
    user_pin = int(input("Please enter your pin: "))

    if user_pin == pin:

        # Display user's cash balance
        print(f"Welcome! Your current balance is ${balance}")
    
        print("Would you like to withdraw or deposit?")
        
        choice = int(input("Select 1. Withdraw 2. Deposit: ")) # The int take input as an integer
        if choice == 1: # User chooses to withdraw
        
            amount = int(input("Please the amount you want to withdraw: ")) # Take input as an integer
            if amount <= balance:# If amount to withdraw is not more than balance
                balance -= amount # Balance = balance - amount
                print("------Withdrawal successful...------")
                print(f"Your updated balance is ${balance}")
            else:
                print("You have insufficient balance")
        elif choice == 2:
            amount = int(input("Please enter the amount you want to deposit: ")) # Take input as an integer
            balance += amount # balance = balance + amount
            
            print("------Deposit successfully...------")
            print(f"Your updated balance is ${balance}")
        else:
            # If the user enters invalid choice
            print("Invalid choice!")
        print("Thank you for transacting business with us")
        break
    number_of_tries -= 1
    if number_of_tries > 0:
        print(f"Incorrect PIN! You have {number_of_tries} attempt(s) left.")
    else:
        print("Access denied! You have exhausted your PIN entry attempts.")