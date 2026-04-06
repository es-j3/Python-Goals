age =  int(input("Enter age of thee: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You're signed up!")
elif age < 0:
    print("You weren't born yet!")
else:
    print("Must be 18+ to sign up.")

response = input("Quieres comida (S/N)?: ")

if response == "Y":
    print("Aqui tienes.")
else:
    print("ok.")

name = input("Enter name: ")

if name == "":
    print("YOU DIDNT TYPE ANYTHING")
else:
    print(f"Hello {name}!")

for_sale = True

if for_sale:
    print("This item is for sale!")
else:
    print("This item isn't for sale.")

sigma = True

if sigma:
    print("Sigma")
else:
    print("Beta")