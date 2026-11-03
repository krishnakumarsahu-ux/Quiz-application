"""
PS 5 - Quiz Application
Language : Python 3
Concepts : Lists, Dictionaries, Loops, Random
Note     : For testing, the questions are asked in this order:
           Q1 'Keyword to define a function?'
           Q2 'len("Hi") = ?'
           Q3 'Mutable type?'
           Pass mark is 50%.
"""

import random

# ---------------- Settings ----------------
NUM_QUESTIONS = 5      # questions asked in a normal (random) quiz
PASS_PERCENTAGE = 50   # pass mark

# For testing set this to True -> only the first 3 questions are asked,
# in fixed order (Q1, Q2, Q3).
# For the real quiz keep it False -> questions are chosen randomly.
TEST_MODE = False
TEST_QUESTIONS = 3

# Question bank: list of dictionaries (question, options, answer)
QUESTION_BANK = [
    {
        "question": "Keyword to define a function?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "B",
    },
    {
        "question": 'len("Hi") = ?',
        "options": ["1", "2", "3", "4"],
        "answer": "B",
    },
    {
        "question": "Mutable type?",
        "options": ["tuple", "str", "list", "int"],
        "answer": "C",
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "B",
    },
    {
        "question": "Which function is used to print output?",
        "options": ["echo()", "print()", "printf()", "write()"],
        "answer": "B",
    },
    {
        "question": "What is the type of the result of 5 / 2 ?",
        "options": ["int", "float", "str", "bool"],
        "answer": "B",
    },
    {
        "question": "Which keyword is used to loop over a sequence?",
        "options": ["for", "repeat", "loop", "iterate"],
        "answer": "A",
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["list", "tuple", "dict", "set"],
        "answer": "C",
    },
    {
        "question": "Which module is used to generate random numbers?",
        "options": ["math", "random", "os", "sys"],
        "answer": "B",
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "C",
    },
    {
        "question": "What is the result of 2 ** 3 ?",
        "options": ["6", "8", "9", "5"],
        "answer": "B",
    },
    {
        "question": "Which of these is NOT a valid variable name?",
        "options": ["my_var", "_count", "2name", "total"],
        "answer": "C",
    },
]

LETTERS = ["A", "B", "C", "D"]


def select_questions():
    """Return the list of questions to ask.
    Test mode: first 3 questions in fixed order.
    Normal mode: random questions using the random module."""
    if TEST_MODE:
        return QUESTION_BANK[:TEST_QUESTIONS]
    return random.sample(QUESTION_BANK, NUM_QUESTIONS)


def show_question(number, q):
    """Print one question with its options."""
    print("\nQ" + str(number) + ". " + q["question"])
    for i in range(len(q["options"])):
        print("  " + LETTERS[i] + ") " + q["options"][i])


def get_answer(number, q):
    """Ask for an answer until a valid option (A/B/C/D) is entered.
    If the option is invalid, the same question is asked again."""
    while True:
        show_question(number, q)
        choice = input("Your answer (A/B/C/D): ").strip().upper()
        if choice in LETTERS:
            return choice
        print("Invalid option. Enter A, B, C or D.")


def ask_question(number, q):
    """Ask one question, check the answer. Returns True if correct."""
    choice = get_answer(number, q)
    if choice == q["answer"]:
        print("Correct!")
        return True
    print("Q" + str(number) + " Wrong. Correct answer: " + q["answer"])
    return False


def show_result(score, total, correct_answers):
    """Show final score, percentage and pass/fail message."""
    percentage = score / total * 100
    if percentage >= PASS_PERCENTAGE:
        result = "Pass"
    else:
        result = "Fail"

    print("\n===== Quiz Result =====")
    print("Score: " + str(score) + "/" + str(total)
          + " | Percentage: " + format(percentage, ".2f") + "%"
          + " | Result: " + result)
    if result == "Fail":
        print("Correct answers: " + ", ".join(correct_answers))


def main():
    print("=== Quiz Application ===")
    questions = select_questions()
    total = len(questions)
    score = 0
    correct_answers = []

    for i in range(total):
        q = questions[i]
        correct_answers.append(q["answer"])
        if ask_question(i + 1, q):
            score += 1

    show_result(score, total, correct_answers)


if __name__ == "__main__":
    main()