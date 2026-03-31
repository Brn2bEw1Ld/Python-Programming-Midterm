import random

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Please enter something.")

def play_student3_game():
    print("\n=== Student 3: Ultimate Game Crossover ===\n")

    game_one = get_input("Enter Student 1's favorite game: ")
    game_two = get_input("Enter Student 2's favorite game: ")
    hero = get_input("Enter a hero or main character: ")
    villain = get_input("Enter a villain or enemy: ")
    special_item = get_input("Enter a special item: ")
    location = get_input("Enter a battle location: ")
    verb = get_input("Enter a verb ending in -ing: ")

    twist = random.choice([
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

def main():
    while True:
        play_student3_game()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Crossover complete!")
            break

main()
