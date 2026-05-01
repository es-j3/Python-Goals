menu = {"ice cream": 4.99,
        "pretzel": 3.99,
        "kabanos": 5.99,
        "zapiekanka": 5.99,
        "water": 0.99,
        "soup": 4.99,
        "fries": 1.99,
        "pizza": 2.99}

cart = []
total = 0

print("~~~ MENU ~~~")
for key, value in menu.items():
    print(f"{key:11}: {value:.2f}")
print("~~~~~~~~~~~~")

while True:
    food = input("What would you like to buy? (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")