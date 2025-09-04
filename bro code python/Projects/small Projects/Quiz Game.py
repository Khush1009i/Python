# Python Quiz game: 

question = ("1.How many colors are there in a rainbow ? ",
       "2.How much grams a 1kg has ? ",
       "3.What is the smallest prime number ? ",
       "4.How many planets are in solar system ? ",
       "5.What is the 10 percent of 100? ",
       )



options = ( 
           ("A.5","B.4","C.7","D.8"),
           ("A.100","B.50","C.400","D.1000"),
           ("A.2","B.1","C.0","D.3"),
           ("A.4","B.7","C.8","D.9"),
           ("A.12","B.15","C.10","D.30"),
           )

answer = ("C", "D", "B", "B", "C")
guesses = []
score = 0
question_num = 0

for que in question:
    print("------------------")
    print(que)
    for opt in options[question_num]:
        print(opt)

    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answer[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect Answer...!")
        print(f"{answer[question_num]} is the correct answer ")
    question_num +=1

print("--------------------------------")
print("             RESULTS            ")
print("--------------------------------")

print("answers: ", end =" ")
for ans in answer:
    print(ans, end=" ")
print()

print("guesses: ", end =" ")
for guesses in guess:
    print(guesses, end=" ")
print()


score = int(score/len(question)*100)
print(f"Your total score is = {score}%")