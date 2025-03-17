import math
import random
from engine.game_engine import run_game


def generate_numbers():
    return [random.randint(1, 100) for _ in range(3)]


def calculate_lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


def generate_question():
    numbers = generate_numbers()
    return " ".join(map(str, numbers))


def get_correct_answer(question):
    numbers = list(map(int, question.split()))
    return calculate_lcm(numbers)


def play_game_gcd():
    game_description = "Find the smallest common multiple of given numbers."
    run_game(game_description, generate_question, get_correct_answer)


if __name__ == "__main__":
    play_game_gcd()
