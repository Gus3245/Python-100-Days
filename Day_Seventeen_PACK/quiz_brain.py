class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_check = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.Checking_question(user_check, current_question.answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def Checking_question(self, user_check , current_answer):
        if user_check.lower() == current_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        
        print(f"The current answer is {current_answer}")
        print(f"The current Score is {self.score}/{self.question_number}")
        print("\n")

       