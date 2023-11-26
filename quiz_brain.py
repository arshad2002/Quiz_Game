class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.mark = 0
        self.question_list = question_list

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {question.text} (True/False): ')
        self.check_answer(answer, question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.mark += 1
            print("You are correct!!")
        else:
            print("You are wrong!!")

        print(f'Correct answer is {correct_answer}')
        print(f'Your mark is {self.mark}/{self.question_number}')
        print("\n")
