import math
import random


def generate_numbers():
    return [random.randint(1, 100) for _ in range(3)]


def calculate_lcm(numbers):
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


def play_game_gcd():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    correct_answers = 0

    while correct_answers < 3:
        numbers = generate_numbers()
        lcm = calculate_lcm(numbers)

        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = input("Your answer: ")
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_answer == lcm:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{lcm}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game_gcd()
