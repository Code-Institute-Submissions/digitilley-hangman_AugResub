import random

def hangman():
    mylist = ["python", "javascript", "react", "github", "django", "bootstrap"]
    secretword = random.choice(mylist)
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
        guess = input()
        if guess in valid_entry:
            userguess = userguess + guess
        else:
            print("Enter a valid character")
            guess = input()
        if guess not in secretword:
            turns = turns - 1

            if turns == 6:
                print("6 turns left!\n")
                print("---------------")
            if turns == 5:
                print("Sorry, that letter isn't in the secret word. 5 turns left!\n")
                print("---------------")
                print("       O       ")
            if turns == 4:
                print("Sorry, that letter isn't in the secret word. 4 turns left!\n")
                print("---------------")
                print("       O       ")
                print("       |       ")
            if turns == 3:
                print("Sorry, that letter isn't in the secret word. 3 turns left!\n")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      /        ")
            if turns == 2:
                print("Sorry, that letter isn't in the secret word. 2 turns left!\n")
                print("---------------")
                print("       O       ")
                print("       |       ")
                print("      / \      ")
            if turns == 1:
                print("Sorry, that letter isn't in the secret word. 1 turn left!\n")
                print("---------------")
                print("       O /     ")
                print("       |       ")
                print("      / \      ")
            if turns == 0:
                print("Oh no! You've run out of turns.\n")
                print("---------------")
                print("       O_|     ")
                print("     / | \     ")
                print("      / \      ")
                print("\nYou lose. Better luck next time!\n")
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
name = str(input("Enter your name: "))
print("\nWelcome, " + name)
print("\nTry to guess the secret word in less than 6 attempts.\n")
hangman()