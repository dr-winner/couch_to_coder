bag = "54"
dress = "60"
shoe = "50"

print("Welcome to our shop! Tell us your budget and we'll suggest what you can afford")
print("How much money do you have on you?")
balance = input("select one of these: Bag = Gh 54, Dress = Gh 60, Shoe = Gh 50:")

if balance == bag:
    print("Please you can afford some nice bag dear!")
elif balance == dress:
    print("Please you can afford the beautiful dress my princess!")
elif balance == shoe:
    print("Oh girl! You can afford the cutiest shoe from us!")
else:
    print("Ooh boy! It seems we do not have any item for you!")