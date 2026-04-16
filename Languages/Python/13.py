#name = input("Enter your full name: ")

#result = len(name)
#result = name.find("x")
#result = name.rfind("l")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = name.isalpha()

#print(result)

#phone_number = input("Enter phone #: ")

#result = phone_number.count("-")
#phone_number = phone_number.replace("-", "")

#print(phone_number)

username = input("Enter username: ")

if len(username) > 12:
    print("Your username cannot be longer than 12 characters!")
elif not username.find(" ") == -1:
    print("Username must not contain spaces!")
elif not username.isalpha():
    print("Username cannot have numbers!")
else:
    print(f"Welcome {username}!")