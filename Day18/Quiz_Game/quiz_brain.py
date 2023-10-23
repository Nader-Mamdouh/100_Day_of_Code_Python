class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_position = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_position.text} (True/False)").lower()
        self.check_answer(user_answer, current_position.answer )

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("you got it all")
        else:
            print("it is wrong answer")
        print(f"the correct answer is {correct_answer}")
        print(f"your current score is {self.score}/ {self.question_number}")
        print("\n")
