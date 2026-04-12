
import random

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Please enter something.")

def play_student1_game():
    print("\n=== Student 1: Favorite Game Adventure ===\n")
    # Collect all user inputs for the madlib story
    player_name = get_input("Enter a player name: ")
    favorite_game = get_input("Enter your favorite video game: ")
    character_type = get_input("Enter a character class or role: ")
    weapon = get_input("Enter a weapon or tool: ")
    location = get_input("Enter a game location: ")
    adjective = get_input("Enter an adjective: ")
    # Random events to help make each story feel slightly different
    event = random.choice([
        "a secret boss suddenly appeared",
        "the screen started shaking from an explosion",
        "a rare loot chest spawned nearby",
        "an NPC yelled for help"
    ])
    # ANSI escape codes for the bold text for the bold text formmating
    bold = "\033[1m"
    reset = "\033[0m"

    bold_cyan = "\033[1;96m"
    bold_green = "\033[1;92m"
    bold_yellow = "\033[1;93m"
    bold_magenta = "\033[1;95m"
    # Table to be able to build the story with user inputs
    story = f"""
{bold}{player_name}{reset} loaded into {bold}{favorite_game}{reset} as a {bold}{character_type}{reset}.
They grabbed their {bold}{adjective}{reset} {bold}{weapon}{reset} and headed toward {bold}{location}{reset}.
Everything seemed normal at first, but then {bold}{event}{reset}.
From that moment on, the adventure became completely wild.
"""
    print(story)

def main():
    while True:
        play_student1_game()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Game over!")
            break

main()
