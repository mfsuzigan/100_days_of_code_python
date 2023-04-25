from ui import QuizInterface
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    QuizInterface(QuizBrain(question_bank))


if __name__ == "__main__":
    main()
