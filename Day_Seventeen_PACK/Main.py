from question_model import Question
from Data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        New_Question = Question(question_text,question_answer)
        question_bank.append(New_Question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

"You've Completed the quiz"
