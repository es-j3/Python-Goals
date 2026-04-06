# kalkulator

operator = input("Choose an operator, Addition (A) Subtraction (S) Multiplication (M) Division (D): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "A":
    result = num1 + num2
    print(result)
elif operator == "S":
    result = num1 - num2
    print(result)
elif operator == "M":
    result = num1 * num2
    print(result)
elif operator == "D":
    result = num1 / num2
    print(result)
else:2
    print(f"This '{operator}' isn't valid Braski!")