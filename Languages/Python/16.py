#name = input("Enter your name: ")

#while name == "":
#    print("You entered nothing!")
#    name = input("Enter your name: ")
#else:
#    print(f"Hello {name}!")

#age = int(input("Enter your age: "))

#while age < 0:
#    print("You weren't born yet! Enter another age")
#    age = int(input("Enter your age: "))

#print(f"You are {age} years old")

#food = input ("enter a food that you like: (q to quit): ")

#while not food == "q":
#    print(f"You like {food}")
#    food = input ("enter another food that you like: (q to quit): ")

#print("Bye!")

num = int(input("Enter number between 1-10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter number between 1-10: "))

print(f"Number's {num}")