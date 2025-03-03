from games.gcd import play_game_gcd
from games.progression import play_game_progression


def show_menu():
    print("Please choose a game to play:")
    print("1. GCD Game")
    print("2. Progression Game")
    print("3. Exit")


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter the number of the game: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 1:
            print("\nStarting GCD Game...\n")
            play_game_gcd()
        elif choice == 2:
            print("\nStarting Progression Game...\n")
            play_game_progression()
        elif choice == 3:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
