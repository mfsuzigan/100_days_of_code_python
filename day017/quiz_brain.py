class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list) - 1

    def print_score(self):
        return f"{self.score}/{self.question_number}"

    def check_answer(self, user_answer, correct_answer):
        answer_was_right = str.lower(user_answer) == str.lower(correct_answer) or str.lower(
            user_answer[0]) == str.lower(correct_answer[0])

        if answer_was_right:
            self.score += 1
            print("Right!")

        else:
            print(f"Thats wrong. Right answer was {correct_answer}.")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        user_answer = input(f"\nQ.{self.question_number + 1}: {current_question.text} (true/false): ")
        self.check_answer(user_answer, current_question.answer)

        print(f"Score: {self.print_score()}")
        self.question_number += 1

        return user_answer
