#Welcome message
print("Welcome to Hangman!")

#Rules
"""
used this article to help with rules section:
https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python
"""
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

#Random Word

