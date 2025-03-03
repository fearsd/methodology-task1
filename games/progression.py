import random


def generate_geometric_progression(start, ratio, length):
    return [start * (ratio**i) for i in range(length)]


def hide_element(progression, index):
    progression[index] = ".."
    return progression


def play_game_progression():
    print("Welcome to the Geometry Progression Game!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    while True:
        start = random.randint(1, 10)
        ratio = random.randint(2, 5)
        length = random.randint(5, 10)
        progression = generate_geometric_progression(start, ratio, length)

        hidden_index = random.randint(0, length - 1)
        hidden_value = progression[hidden_index]
        progression_with_hidden = hide_element(progression.copy(), hidden_index)

        print("What number is missing in the progression?")
        print("Question:", " ".join(map(str, progression_with_hidden)))

        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_answer == hidden_value:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_value}'."
            )
            print(f"Let's try again, {name}!")
            break

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game_progression()
