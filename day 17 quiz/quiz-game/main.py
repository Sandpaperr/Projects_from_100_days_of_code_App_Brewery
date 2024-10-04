# This code is built upon a skeleton provided by App Brewery.
# Modifications and further implementations were done by Leandro.
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def quiz_game():

    question_bank = []

    # Create quiz bank
    for dictionary in question_data:
        text = dictionary["question"]
        answer = dictionary["correct_answer"]
        question_obj = Question(text, answer)

        question_bank.append(question_obj)

    quiz = QuizBrain(question_bank)

    while quiz.has_still_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score is {quiz.score}/{quiz.question_number}")




quiz_game()