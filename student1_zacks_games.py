
import random

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Please enter something.")

def play_student1_game():
    print("\n=== Student 1: Favorite Game Adventure ===\n")

    player_name = get_input("Enter a player name: ")
    favorite_game = get_input("Enter your favorite video game: ")
    character_type = get_input("Enter a character class or role: ")
    weapon = get_input("Enter a weapon or tool: ")
    location = get_input("Enter a game location: ")
    adjective = get_input("Enter an adjective: ")

    event = random.choice([
        "a secret boss suddenly appeared",
        "the screen started shaking from an explosion",
        "a rare loot chest spawned nearby",
        "an NPC yelled for help"
    ])
    
    bold = "\033[1m"
    reset = "\033[0m"

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
