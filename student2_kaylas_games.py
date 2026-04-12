import random
import json
import os

# Kayla's section of the Midterm Mad Lib Project

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "madLibWords.json")

# Set global scope variables
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

# Complete story prompt, returning the dictionary so it can be written to madLibWords.json
def storyPrompt(madLibWords):
    madLibWords["k_playerName"] = wordPrompt("Enter a player name: ")
    madLibWords["k_gameTitle"] = wordPrompt("Enter the title to a game: ")
    madLibWords["k_numMonst"] = numberPrompt("Enter a whole number: ")
    madLibWords["k_descMonst"] = wordPrompt("Enter an adjective: ")
    madLibWords["k_enemy"] = wordPrompt("Enter a type of enemy: ")
    madLibWords["k_emotion"] = wordPrompt("Enter an emotion: ")
    madLibWords["k_reaction"] = wordPrompt("Enter a reaction(sigh, scream, laugh, etc): ")

    # Generate a random choice, just for fun
    madLibWords["k_problem"] = random.choice([
        "the world crumbled, becoming a vast void",
        "many enemies surrounded them, with nowhere to run",
        "they were teleported away",
        "they began to fly, flying away from the chaos"
        ])
    # Generate story
    story = f"""
    {bold_cyan}{madLibWords["k_playerName"]}{reset} burst into a new world, the world of {bold_cyan}{madLibWords["k_gameTitle"]}{reset}.
    Suddenly, {bold_cyan}{madLibWords["k_numMonst"]}{reset} {bold_cyan}{madLibWords["k_descMonst"]}{reset} {bold_cyan}{madLibWords["k_enemy"]}{reset}s appeared.
    Feeling overcome with {bold_cyan}{madLibWords["k_emotion"]}{reset}, {bold_cyan}{madLibWords["k_playerName"]}{reset} let out a {bold_cyan}{madLibWords["k_reaction"]}{reset}.
    Then in an instant, {bold_cyan}{madLibWords["k_problem"]}{reset}.
    """
    # Print the story
    print(story)
    return(madLibWords)

def main():
    # Try to open the json file, if it doesnt exist, create a new dictionary
    try:
        with open(file_path) as f:
            madLibWords = json.load(f)
    except FileNotFoundError:
        madLibWords = {}

    # If json file is already filled, ask if the player would like to keep data
    if "k_playerName" in madLibWords:
        print("Previous data found.")
        print()
        print(f"""
            {bold_cyan}{madLibWords["k_playerName"]}{reset} burst into a new world, the world of {bold_cyan}{madLibWords["k_gameTitle"]}{reset}.
            Suddenly, {bold_cyan}{madLibWords["k_numMonst"]}{reset} {bold_cyan}{madLibWords["k_descMonst"]}{reset} {bold_cyan}{madLibWords["k_enemy"]}{reset}s appeared.
            Feeling overcome with {bold_cyan}{madLibWords["k_emotion"]}{reset}, {bold_cyan}{madLibWords["k_playerName"]}{reset} let out a {bold_cyan}{madLibWords["k_reaction"]}{reset}.
            Then in an instant, {bold_cyan}{madLibWords["k_problem"]}{reset}.
            """)
        print()
        ans = input("Would you like to keep current data? (y/n)").strip().lower()
        if ans == "y": # Keep data
            print("Keeping current data. Thank you for playing.")
        else: # Rewrite data
            madLibWords = storyPrompt(madLibWords)
            with open(file_path, "w") as f:
                json.dump(madLibWords, f, indent=4)
    else: # No previous data found, run program and save in json
        print("No previous data found.")
        madLibWords = storyPrompt(madLibWords)
        with open(file_path, "w") as f:
            json.dump(madLibWords, f, indent=4)
    input("Press enter to close.")

# Calling Main
main()
