def run_game(game_description, generate_question, get_correct_answer):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_description)

    correct_answers = 0
    max_rounds = 3

    while correct_answers < max_rounds:
        question = generate_question()
        correct_answer = get_correct_answer(question)

        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
