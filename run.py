import random


def hangman():
    # List of words
    mylist = ["python", "javascript", "react", "github", "django", "bootstrap"]
    # Selects word from myList at random with each new game
    secretword = random.choice(mylist)
    # Number of turns user gets
    turns = 6
    userguess = ""
    valid_entry = set("abcdefghijklmnopqrstuvwxyz")

    while len(secretword) > 0:
        main_word = ""
        for letter in secretword:
            if letter in userguess:
                main_word = main_word + letter
            else:
                main_word = main_word + "_ "
        if main_word == secretword:
            print(main_word)
            print("Hurray! You guessed the secret word. You win!!!!")
            break
        print("\nPick a letter...", main_word)
        guess = input("\n")
        if guess in valid_entry:
            userguess = userguess + guess
        else:
            print("Enter a valid character")
            guess = input("\n")
        if guess not in secretword:
            turns = turns - 1

            if turns == 6:
                print("\nSorry, try again. 6 turns left!")
                print("---------------")
            if turns == 5:
                print("\nSorry, try again. 5 turns left!")
                print("---------------")
                print("       O       ")
            if turns == 4:
                print("\nSorry, try again. 4 turns left!")
                print("---------------")
                print("       O       ")
                print("       |       ")
            if turns == 3:
                print("\nSorry, try again. 3 turns left!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            if turns == 2:
                print("\nSorry, try again. 2 turns left!")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns == 1:
                print("\nSorry, try again. 1 turn left!")
                print("---------------")
                print("       O /     ")
                print("       |       ")
                print("      / \      ")
            if turns == 0:
                print("\nOh no! You've run out of turns.")
                print("---------------")
                print("       O_|     ")
                print("     / | \     ")
                print("      / \      ")
                print("\nYou lose. Better luck next time!")
                break

# Welcome message
print("Welcome to Hangman!")
# Rules
rules = """
The aim of the game is to correctly guess the secret word...
Guess a letter to begin. If it's correct, the letter will be displayed.
If you guess incorrectly, you lose a life. You get a total of 6 lives.
-----------------------------------------------------------------------
"""
print(rules)
# Enter name
while True:
        name = input("What is your name? ")

        if not name.isalpha():
            print("\nPlease pick a letter from the alphabet.")
            continue
        else:
            print("\nWelcome, " + name)
            print("\nTry to guess the secret word in less than 6 attempts.")
            hangman()
            break
