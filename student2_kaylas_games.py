import random

# Kayla's section of the Midterm Mad Lib Project

# Checks if the given input is empty
def isEmpty(given):
    if given == "":
        print("That is an invalid value. Please try again.")
        return True
    else:
        return False

# Get the user to input a number, ask again if value isn't a whole number
# Accepts any value that is a whole number.
def numberPrompt(prompt):
    given = input(prompt).strip()
    try:
        return int(given)
    except:
        print("That wasn't a number. Please try again.")
        return numberPrompt(prompt)

# Get the user input and ask again if the given value is empty
# Accepts any value that isn't a space
def wordPrompt(prompt):
    given = input(prompt).strip()
    if isEmpty(given):
        return wordPrompt(prompt)
    return given

# Main Code

playerName = wordPrompt("Enter a player name: ")
gameTitle = wordPrompt("Enter the title to a game: ")
numMonst = numberPrompt("Enter a whole number: ")
descMonst = wordPrompt("Enter an adjective: ")
enemy = wordPrompt("Enter a type of enemy: ")
emotion = wordPrompt("Enter an emotion: ")
reaction = wordPrompt("Enter a reaction(sigh, scream, laugh, etc): ")

bold = "\033[1m"
reset = "\033[0m"

green = "\033[92m"
cyan = "\033[96m"
yellow = "\033[93m"
magenta = "\033[95m"

bold_cyan = "\033[1;96m"
bold_green = "\033[1;92m"
bold_yellow = "\033[1;93m"
bold_magenta = "\033[1;95m"

problem = random.choice([
    "the world crumbled, becoming a vast void",
    "many enemies surrounded them, with nowhere to run",
    "they were teleported away",
    "they began to fly, flying away from the chaos"
    ])

story = f"""
{bold_cyan}{playerName}{reset} burst into a new world, the world of {bold_cyan}{gameTitle}{reset}.
Suddenly, {bold_cyan}{numMonst}{reset} {bold_cyan}{descMonst}{reset} {bold_cyan}{enemy}{reset}s appeared.
Feeling overcome with {bold_cyan}{emotion}{reset}, {bold_cyan}{playerName}{reset} let out a {bold_cyan}{reaction}{reset}.
Then in an instant, {bold_cyan}{problem}{reset}.
"""

print(story)
