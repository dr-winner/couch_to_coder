bag = "54"
dress = "60"
shoe = "50"
# 
print("How much money do you have on you?")
print("select one of these: Bag = Gh 54, Dress = Gh 60, Shoe = Gh 50:")
# input()
balance = input()
# print("What do you want to buy?")
# input()
# cost_item = input()
if balance == bag:
    print("Please you can afford some nice bag dear!")
elif balance == dress:
    print("Please you can afford the beautiful dress my princess!")
elif balance == shoe:
    print("Oh girl! You can afford the cutiest shoe from us!")
else:
    print("Ooh boy! It seems we do not have any item for you!")