import math
import random
from engine.game_engine import run_game


def generate_numbers():
    return [
        random.randint(1, 20) for _ in range(2)
    ]  # Генерируем два числа для простоты


def calculate_lcm(numbers):
    return math.lcm(numbers[0], numbers[1])  # Используем math.lcm для вычисления НОК


def generate_question_and_answer():
    numbers = generate_numbers()
    question = " ".join(map(str, numbers))
    correct_answer = calculate_lcm(numbers)
    return question, correct_answer


def play_game_lcm():
    game_description = "Find the least common multiple of given numbers."
    run_game(game_description, generate_question_and_answer)


if __name__ == "__main__":
    play_game_lcm()
