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
{bold_cyan}{madLibWords["z_hero"]}{reset} was traveling through {bold_green}{madLibWords["z_favoriteGame"]}{reset}
when a portal ripped open and pulled them into the world of {bold_green}{madLibWords["k_gameTitle"]}{reset}.

At the same time, {bold_cyan}{madLibWords["k_playerName"]}{reset} was surrounded by
{bold_yellow}{madLibWords["k_numMonst"]}{reset} {bold_yellow}{madLibWords["k_descMonst"]}{reset}
{bold_yellow}{madLibWords["k_enemy"]}s{reset} and barely holding on.

With the powerful {bold_magenta}{madLibWords["z_specialItem"]}{reset} in hand,
{bold_cyan}{madLibWords["z_hero"]}{reset} landed in {bold_green}{madLibWords["c_loc"]}{reset}
just as {bold_yellow}{madLibWords["z_event"]}{reset}.

While {bold_yellow}{madLibWords["c_verb"]}{reset}, the two heroes discovered the legendary
{bold_magenta}{madLibWords["c_item"]}{reset}, but before they could escape,
{bold_magenta}{madLibWords["c_villain"]}{reset} appeared beside
{bold_magenta}{madLibWords["z_villain"]}{reset}.

Feeling {bold_yellow}{madLibWords["k_emotion"]}{reset}, {bold_cyan}{madLibWords["k_playerName"]}{reset}
let out a loud {bold_yellow}{madLibWords["k_reaction"]}{reset} as
{bold_yellow}{madLibWords["k_problem"]}{reset}.

Then {bold_magenta}{madLibWords["c_twist"]}{reset}, turning the crossover between
{bold_green}{madLibWords["z_gameTwo"]}{reset} and {bold_green}{madLibWords["k_gameTitle"]}{reset}
into the ultimate gaming showdown.
"""
    print(story)
    return madLibWords
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
            print(f"""
{bold_cyan}{madLibWords["z_hero"]}{reset} was traveling through {bold_green}{madLibWords["z_favoriteGame"]}{reset}
when a portal ripped open and pulled them into the world of {bold_green}{madLibWords["k_gameTitle"]}{reset}.

At the same time, {bold_cyan}{madLibWords["k_playerName"]}{reset} was surrounded by
{bold_yellow}{madLibWords["k_numMonst"]}{reset} {bold_yellow}{madLibWords["k_descMonst"]}{reset}
{bold_yellow}{madLibWords["k_enemy"]}s{reset} and barely holding on.

With the powerful {bold_magenta}{madLibWords["z_specialItem"]}{reset} in hand,
{bold_cyan}{madLibWords["z_hero"]}{reset} landed in {bold_green}{madLibWords["c_loc"]}{reset}
just as {bold_yellow}{madLibWords["z_event"]}{reset}.

While {bold_yellow}{madLibWords["c_verb"]}{reset}, the two heroes discovered the legendary
{bold_magenta}{madLibWords["c_item"]}{reset}, but before they could escape,
{bold_magenta}{madLibWords["c_villain"]}{reset} appeared beside
{bold_magenta}{madLibWords["z_villain"]}{reset}.

Feeling {bold_yellow}{madLibWords["k_emotion"]}{reset}, {bold_cyan}{madLibWords["k_playerName"]}{reset}
let out a loud {bold_yellow}{madLibWords["k_reaction"]}{reset} as
{bold_yellow}{madLibWords["k_problem"]}{reset}.

Then {bold_magenta}{madLibWords["c_twist"]}{reset}, turning the crossover between
{bold_green}{madLibWords["z_gameTwo"]}{reset} and {bold_green}{madLibWords["k_gameTitle"]}{reset}
into the ultimate gaming showdown.
""")
            ans = input("Would you like to keep current data? (y/n)")
            if ans == "y":
                print("Keeping current data. Thank you for playing.")
            else:   
                madLibWords = play_student3_game(madLibWords)
                with open(file_path, "w") as f:
                    json.dump(madLibWords, f, indent=4)
        else:
            madLibWords = play_student3_game(madLibWords)
            with open(file_path, "w") as f:
                json.dump(madLibWords, f, indent=4)
    else:
        print("No previous data found.")
        print("Please ensure both Zack's and Kayla's")
        print("programs were previously ran.")
        print("Closing Program.")

main()
input("Press Enter to Close...")
