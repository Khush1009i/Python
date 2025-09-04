# Membership operator = used to test whether a value or var is found in seq
# (string, list, tuple, set, dictionary)
# in & not it

word = "APPLE"

letter = input("guess a letter in the secret word: ")

if letter not in word:
    print(f"yes, the letter is not in the word {letter}")
else:
    print(f"{letter} not found")




students = { "Sponge", "patrick", "Andy", "Sandy"}
student = input("Enter the name of the student: ")


if student in students:
    print(F"{student} is a student")
else:
    print(f"{student} was not a student")



grades = {"Sandy":"A", "Khush":"B", "Andy":"C"}

student = input("Enter the name of the student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} not Found...!!!!")


email = "sonikhush@gmail.com"

if "@"  and ".com" in email:
    print(f"It's a valid email")
else:
    print("It's not a email")