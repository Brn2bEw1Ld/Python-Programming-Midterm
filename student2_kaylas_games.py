
import random

def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Please enter something.")

def play_student2_game():
    print("\n=== Student 2: Favorite Game Challenge ===\n")

    player_name = get_input("Enter a player name: ")
    favorite_game = get_input("Enter your favorite video game: ")
    enemy = get_input("Enter an enemy or monster: ")
    item = get_input("Enter a healing item or power-up: ")
    game_mode = get_input("Enter a game mode: ")
    emotion = get_input("Enter an emotion: ")

    problem = random.choice([
        "the controller disconnected at the worst possible moment",
        "all the enemies suddenly became twice as strong",
        "the map changed without warning",
        "a teammate accidentally triggered the alarm"
    ])

    story = f"""
{player_name} was playing {favorite_game} in {game_mode} mode.
Out of nowhere, a terrifying {enemy} appeared.
They quickly reached for their {item}, feeling extremely {emotion}.
Then {problem}, and the whole match turned into chaos.
"""
    print(story)

def main():
    while True:
        play_student2_game()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Match ended!")
            break

main()
