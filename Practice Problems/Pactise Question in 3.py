# WAP to print each line of a file  in reverrse order
string = "Khush"

# I method: 
# print("".join(reversed(string)))

# II method:
# print(string[::-1])


# WAP to compute number of character, words, lines
# Get input from user
# while True:
#     print("What would you like to write (press n for name/ s for sentence)")
#     print()
#     choice = input("Enter your choice: ").strip().lower()
#     if choice == "n":
#         name = input("Enter your name: ").strip()
#         # Count characters and words
#         num_chars = len(name)          # Total characters including spaces
#         num_words = len(name.split())  # Split by spaces to count words

#         print(f"Number of characters: {num_chars}")
#         print(f"Number of words: {num_words}")
#         break
        
#     elif choice == "s":
#         sentence = input("Write any sentence {without pressing enter}: ").strip()
#         total_chars = len(sentence)
#         total_words = len(sentence.split() )

#         print(f"Number of character in the sentence : {total_chars}")
#         print(f"Total words in the sentence: {total_words}")
#         break
#     else:
#         print("Sorry, Invalid choice...!")
#         print("Lets try again")
#         print()


while True:
    choice = input("Press 'n' for Name or 's' for Sentence: ").strip().lower()
    if choice in ["n", "s"]:
        text = input("Enter your name: " if choice == "n" else "Enter a sentence: ").strip()
        print(f"\nNumber of characters: {len(text)} \nNumber of words: { len(text.split()) } ")
        break
    print("\nInvalid choice, try again.")

