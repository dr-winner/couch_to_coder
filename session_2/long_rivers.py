rivers = [
 {"name": "Nile", "length": 4157},
 {"name": "Yangtze", "length": 3434},
 {"name": "Murray-Darling", "length": 2310},
 {"name": "Volga", "length": 2290},
 {"name": "Mississippi", "length": 2540},
 {"name": "Amazon", "length": 3915}
]

# printing each river's name:

for river in rivers:
    print(river["name"])

# total length of all rivers:

total_length = 0
for river in rivers:
    total_length += river["length"]
print(f"The total length of all rivers is {total_length} miles")

# rivers that begin with M:

print("Rivers beginning with M:")
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])

# converting from miles to kilometers:

for river in rivers:
    length_in_km = river["length"] * 1.6
    print(f"{river['name']} - Length: {length_in_km:.2f} km")