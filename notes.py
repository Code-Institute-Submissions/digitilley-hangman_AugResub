"""
# Loop until incorrectAnswers = 6
# Player wins if they guess the word before using up their 6 lives
while incorrectAnswers > 0:

    # Player to guess a letter
    guess = input("\nPick a letter: ")
    if guess in hiddenWord:
        print(f"\nCorrect! There are one or more {guess}'s in the word.")
    else:
        incorrectAnswers -= 1
        print(f"\n{guess} is incorrect. {incorrectAnswers} turn(s) left.")
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
"""