
import random
import json

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Please enter something.")

def play_student1_game(madLibWords):
    print("\n=== Student 1: Favorite Game Adventure ===\n")
    
    # Collect all user inputs for the madlib story
    
    madLibWords["z_favoriteGame"] = get_input("Enter your favorite video game: ")
    madLibWords["z_gameTwo"] = get_input("Enter another game title: ")
    madLibWords["z_hero"] = get_input("Enter a hero or main character: ")
    madLibWords["z_villain"] = get_input("Enter a villain or enemy: ")
    madLibWords["z_specialItem"] = get_input("Enter a special item: ")
    madLibWords["z_location"] = get_input("Enter a battle location: ")
    madLibWords["z_verb"] = get_input("Enter a verb ending in -ing: ")
    
    # Random events to help make each story feel slightly different
    
    madLibWords ["z_event"] = random.choice([
        "a secret boss suddenly appeared",
        "the screen started shaking from an explosion",
        "a rare loot chest spawned nearby",
        "an NPC yelled for help"
    ])
    
    # ANSI escape codes for the bold text for the bold text formmating
    
    bold = "\033[1m"
    reset = "\033[0m"
    
    # These are used to make the specific madlib words stand and pop out visually when printed
    
    bold_cyan = "\033[1;96m"
    bold_green = "\033[1;92m"
    bold_yellow = "\033[1;93m"
    bold_magenta = "\033[1;95m"
    
    # Table to be able to build the story with user inputs
    
    story = f"""
{bold_cyan}{madLibWords["z_hero"]}{reset} loaded into {bold_green}{madLibWords["z_favoriteGame"]}{reset} and crossed into {bold_green}{madLibWords["z_gameTwo"]}{reset}.
Armed with a {bold_magenta}{madLibWords["z_specialItem"]}{reset}, they headed toward {bold_green}{madLibWords["z_location"]}{reset}.
Everything seemed normal at first, but then {bold_yellow}{madLibWords["z_event"]}{reset}.
From that moment on, the adventure became completely wild.
"""
    print(story)
    return madLibWords

def main():
    # Try to load existing data
    try:
        with open("madLibWords.json", "r") as f:
            madLibWords = json.load(f)
    except FileNotFoundError:
        madLibWords = {}

    while True:
        # Run your story and get updated data
        madLibWords = play_student1_game(madLibWords)

        # Save updated data back to JSON file
        with open("madLibWords.json", "w") as f:
            json.dump(madLibWords, f, indent=4)

        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Game over!")
            break

main()
