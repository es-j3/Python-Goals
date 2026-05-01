import random

lowest_num = 1
highest_num = 101
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Number guessing game!")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("Number is out of range!")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"Congrats you got it! The answer was {answer}")
            print(f"You took {guesses} guesses.")
            is_running = False

    elif guess == "q" or "Q":
        print("Goodbye!")
        is_running = False
    else:
        print("Invalid guess!")
        print(f"Select an integer (number) between {lowest_num} and {highest_num}")