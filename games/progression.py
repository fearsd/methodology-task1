import random
from engine.game_engine import run_game


def generate_geometric_progression(start, ratio, length):
    return [start * (ratio**i) for i in range(length)]


def hide_element(progression, index):
    progression[index] = ".."
    return progression


def generate_question_and_answer():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = generate_geometric_progression(start, ratio, length)

    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression_with_hidden = hide_element(progression.copy(), hidden_index)

    question = " ".join(map(str, progression_with_hidden))
    return question, hidden_value


def play_game_progression():
    game_description = "What number is missing in the progression?"
    run_game(game_description, generate_question_and_answer)


if __name__ == "__main__":
    play_game_progression()
