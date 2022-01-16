#Welcome message
print("Welcome to Hangman!")

#Rules
rules = """
The aim of the game is to correctly guess the random word...

Guess a letter to begin. If it's correct, the letter will be displayed.

If you guess incorrectly, you will lose 1 life. You get a total of 6 lives.
"""
print(rules)

#Player name
name = str(input("Enter your name: "))

#Good luck message
print("\nGood luck, "+ name)


