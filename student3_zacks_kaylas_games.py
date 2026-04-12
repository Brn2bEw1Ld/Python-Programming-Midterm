import random
import json
import os

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

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Please enter something.")

def play_student3_game(madLibWords):
    print("\n=== Student 3: Ultimate Game Crossover ===\n")

    madLibWords["c_villain"] = get_input("Enter a villain or enemy: ")
    madLibWords["c_item"] = get_input("Enter a special item: ")
    madLibWords["c_loc"] = get_input("Enter a battle location: ")
    madLibWords["c_verb"] = get_input("Enter a verb ending in -ing: ")

    madLibWords["c_twist"] = random.choice([
        "the worlds merged into one giant battlefield",
        "a final boss spawned from another dimension",
        "the scoreboard exploded with bonus points",
        "every NPC started cheering for the hero"
    ])

    story = f"""
In a crazy crossover between {game_one} and {game_two}, {hero} entered {location}.
There they found the powerful {special_item} while {verb}.
Suddenly, {villain} appeared and attacked without warning.
Then {twist}, turning the battle into the ultimate gaming showdown.
"""
    print(story)

def checkPreviousPrograms(madLibWords):
    if "z_hero" in madLibWords and "k_playerName" in madLibWords:
        return True
    else:
        return False
        
def main():
    try:
        with open(file_path) as f:
            madLibWords = json.load(f)
    except FileNotFoundError:
        madLibWords = {}

    if checkPreviousPrograms(madLibWords):
        if "c_villain" in madLibWords:
            print("Previous data found.")
            print()
            print()#Insert story here as well
            ans = input("Would you like to keep current data? (y/n)")
            if ans == "y":
                print("Keeping current data. Thank you for playing.")
            else:   
                play_student3_game(madLibWords)
                with open(file_path, "w") as f:
                    json.dump(madLibWords, f, indent=4)
    else:
        print("No previous data found.")
        print("Please ensure both Zack's and Kayla's")
        print("programs were previously ran.")
        print("Closing Program.")

main()
