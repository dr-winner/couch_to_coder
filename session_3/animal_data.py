animals = [
    {
        "name": "capybara",
        "group": "rodent",
        "weight": 140,
    },
    {
        "name": "hedgehog",
        "group": "mammal",
        "weight": 1.5,
    },
    {
        "name": "bearded dragon",
        "group": "reptile",
        "weight": 5,
    },
    {
        "name": "tortoise",
        "group": "reptile",
        "weight": 100,
    },
    {
        "name": "hummingbird",
        "group": "bird",
        "weight": 0.02,
    },
    {
        "name": "elephant",
        "group": "mammal",
        "weight": 6000,
    },
    {
        "name": "ostrich",
        "group": "bird",
        "weight": 150,
    },
    {
        "name": "python",
        "group": "reptile",
        "weight": 200,
    },
    {
        "name": "blue whale",
        "group": "mammal",
        "weight": 200000,
    },
    {
        "name": "lion",
        "group": "mammal",
        "weight": 250,
    },
]

# Printing out the heaviest animal
heaviest_animal = animals[0]

for animal in animals:
    if (animal["weight"] > heaviest_animal["weight"]):
        heaviest_animal = animal

print(heaviest_animal)

# Printing out the lightest animal
lightest_animal = animals[0]

for animal in animals:
    if (animal["weight"] < lightest_animal["weight"]):
        lightest_animal = animal

print(lightest_animal)

# Printing all mammals

mammals = []
for animal in animals:
    if (animal["group"] == "mammal"):
        mammals.append(animal)
        
print(mammals)

animals_with_long_names = []
for animal in animals:
    if (len(animal["name"]) > 7):
        animals_with_long_names.append(animal)
print(animals_with_long_names)