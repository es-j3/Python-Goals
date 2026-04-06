location = input("Where is the banana?: ")
age = int(input("How old are you?: "))

age += 1

print(f"The banana is {location}")
print("Happy birthday")
print(f"You are {age} years old!!")

print("Alright, welcome to the L*W FINDER")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"Die area ist: {area}")

print("SHOPPING CART PROGRAM")

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("Quantity of desired product?: "))
total = price * quantity

print(f"You are buying {quantity} {item}/s costing {price} each, your total will be {total}zl")