import random
mylist = ["python", "javascript", "react", "github", "django", "bootstrap"]

# Welcome message
print("Welcome to Hangman!")

# Rules
"""
used this article to help with rules section:
https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python
"""
rules = """
The aim of the game is to correctly guess the hidden word...

Guess a letter to begin. If it's correct, the letter will be displayed.

If you guess incorrectly, you lose a life. You get a total of 6 lives.
-----------------------------------------------------------------------
"""
print(rules)

# Player name
name = str(input("Enter your name: "))

# Good luck message
print("\nGood luck, " + name)

"""
Article used to help with random.choice:
https://stackoverflow.com/questions/306400/how-can-i-randomly-select-an-item-from-a-list
"""
hiddenWord = random.choice(mylist)
lettersGuessed = ""

# The number of incorrect answers before the player loses
incorrectAnswers = 6

# Loop until incorrectAnswers = 6
# Player wins if they guess the word before using up their 6 lives
while incorrectAnswers > 0:

    # Player to guess a lettera
    guess = input("\nPick a letter: ")
    if guess in hiddenWord:
        print(f"\nCorrect! There are one or more {guess}'s in the word.")
    else:
        incorrectAnswers -= 1
        print(f"\n{guess} is incorrect.{incorrectAnswers} turn(s) left.")
    # list of letters guessed
    lettersGuessed = lettersGuessed + guess
    incorrectLetterCount = 0

    for letter in hiddenWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            incorrectLetterCount += 1
    print("")
    # If there were no wrong letters, the player wins!
    if incorrectLetterCount == 0:
        print(f"\nCongrats, {name}! {hiddenWord} is correct. You win.")
        break
# If the player uses up their 6 lives, they lose!
else:
    print(f"\nSorry you ran out of guesses! Better luck next time, {name}.")
