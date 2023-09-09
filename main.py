# Made by @SorrySSB on twitter. Snake still sucks.

# Self explanatory
import csv  # Allows us to use a CSV file to make a list of dicts
import random  # Allows us to generate a random number so we can guess a random character

# variables
charList = []
win = False

# opens the CSV and writes the contents to a dict
with open('Characters.csv', 'r') as file:
    reader = csv.DictReader(file)
    charList = list(reader)

# Uses a random number to choose a random character
randChar = charList[random.randint(0, 88)]

# converts the strings to numbers to avoid weird behavior when comparing strings
for row in charList:
    row['FallSpeed'] = float(row['FallSpeed'])
    row['Weight'] = int(row['Weight'])
    row['RunSpeed'] = float(row['RunSpeed'])
    row['OOSSpeed'] = int(row['OOSSpeed'])


# Functions to check each value and displays whether it's higher, lower, or the same
def TierCheck(guessedChar):
    if guessedChar['Tier'] > randChar['Tier']:
        print("My character is a Higher tier")
    elif guessedChar['Tier'] < randChar['Tier']:
        print("My character is a Lower Tier")
    elif guessedChar['Tier'] == randChar['Tier']:
        print("My character is the same tier")


def FallSpeedCheck(guessedChar):
    if guessedChar['FallSpeed'] > randChar['FallSpeed']:
        print("My character has a Slower Fall Speed")
    elif guessedChar['FallSpeed'] < randChar['FallSpeed']:
        print('My character has a Faster Fall Speed')
    elif guessedChar['FallSpeed'] == randChar['FallSpeed']:
        print("My character has the same Fall Speed")


def WeightCheck(guessedChar):
    if guessedChar['Weight'] > randChar['Weight']:
        print("My character is lighter")
    elif guessedChar['Weight'] < randChar['Weight']:
        print('My character is heavier')
    elif guessedChar['Weight'] == randChar['Weight']:
        print("My character is the same weight")


def RunSpeedCheck(guessedChar):
    if guessedChar['RunSpeed'] > randChar['RunSpeed']:
        print("My character runs slower")
    elif guessedChar['RunSpeed'] < randChar['RunSpeed']:
        print('My character runs faster')
    elif guessedChar['RunSpeed'] == randChar['RunSpeed']:
        print("My character runs at the same speed")


def OOSSpeedCheck(guessedChar):
    if guessedChar['OOSSpeed'] > randChar['OOSSpeed']:
        print("My character's fastest OOS option is faster")
    elif guessedChar['OOSSpeed'] < randChar['OOSSpeed']:
        print('My character\'s fastest OOS option is slower')
    elif guessedChar['OOSSpeed'] == randChar['OOSSpeed']:
        print("My character's fastest OOS option is the same speed")


# prompt
print("I'm thinking of a character.")

guesses = 0

# Main loop
while not win:
    try:
        print("Guesses: " + ("X" * (5 - guesses)))

        # Where the user guesses the character. Makes it lowercase cause a character name shouldnt be case sensitive
        guess = input("Guess a character: ").lower()

        # stole this from stackoverflow idk what it does but it works LMAO
        # like it checks the guessed character's name against the randomly generated name
        # but past that this is greek to me
        guessedChar = next(item for item in charList if item["Name"].lower() == guess)

        # Runs checks, prints how close you were
        TierCheck(guessedChar)
        FallSpeedCheck(guessedChar)
        WeightCheck(guessedChar)
        RunSpeedCheck(guessedChar)
        OOSSpeedCheck(guessedChar)

        # increments guesses so you only have 5 tries.
        guesses += 1

        # If you win
        if guessedChar['Name'] == randChar["Name"]:
            win = True
            print("You Won! The character was: " + randChar["Name"])
            break
        # If you lose by running outta guesses
        if guesses >= 5:
            print("You Lost...")
            print("The character was: " + randChar["Name"])
            break
    # catches you if you mistype something
    except Exception as ex:
        print("We had an error", str(ex))

