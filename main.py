from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import html

question_bank = []
for question in question_data["results"]:
    question_bank.append(Question(html.unescape(question["question"]), question["correct_answer"]))

quizz = QuizBrain(question_bank)
while quizz.still_has_question():
    quizz.next_question()

print("Congo!! You have finished the quiz")
print(f"Your final score is {quizz.mark}/{quizz.question_number}")
