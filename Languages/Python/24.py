questions = ("What is the largest ocean?: ",
             "What is the capital of Poland?:",
             "What year is Ethiopia in?: ",
             "How many planets are there?: ",
             "An apple a day keeps who away?: ")

options = (("A. Indian Ocean", "B. Atlantic Ocean", "C. Baltic Sea", "D. Pacific Ocean"),
           ("A. Prague", "B. Warsaw", "C. Budapest", "D. Paris"),
           ("A. 100", "B. 2017", "C. 2026", "D. 2018"),
           ("A. 8", "B. 9", "C. 7", "D. 30"),
           ("A. Adin Ross", "B. Bill Gates", "C. Zuck", "D. Doctor"))

answers = ("D", "B", "D", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("~~~~~~~~~~~~~~~~~")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECTUMUNDO!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~RESULTS~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~")

print("answers: ", end="")
for answer in answers:
    print(answer, end= " ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end= " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")