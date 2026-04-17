principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the interest amount: "))
    if principle < 0:
        print("Principle cannot be less than 0!")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Okay bro you would be losing money, don't enter below zero!")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if rate < 0:
        print("We cannot go back in time, sorry!")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")