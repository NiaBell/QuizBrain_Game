from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

bank=[]
for items in question_data:
    question_text=items["text"]
    answer_text=items["answer"]
    newQuestion=Question(question_text,answer_text)
    bank.append(newQuestion)

quiz=QuizBrain(bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

quiz.quiz_end()