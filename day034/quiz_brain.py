import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        next_question = None

        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            next_question = f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

        return next_question

    def answer_is_correct(self, user_answer: bool) -> bool:
        correct_answer = self.current_question.answer
        answer_is_correct = user_answer == eval(correct_answer)

        if answer_is_correct:
            self.score += 1

        return answer_is_correct
