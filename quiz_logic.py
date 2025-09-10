# quiz_logic.py
"""Quiz logic for the U_Think_U_know_Islam quiz"""
from questions import quiz_questions

MAX_LEVEL = 15


class Quiz:
    """Class managing the quiz flow"""
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions


class Player:
    """Class representing a player taking the quiz"""

    def __init__(self,
                 name,
                 level=1,
                 quiz=Quiz(name="U_Think_U_know_Islam", questions=quiz_questions)
                 ):
        self.name = name
        self.level = level
        self.quiz = quiz

    def start_quiz(self):
        """method handling when quiz begins"""
        print(f"""
              Hello {self.name}! Welcome to {self.quiz.name} Quiz Game!
              Please Follow instructions as follow:
                - You will see question appear on the screen with 4 options a, b, c, and d
                - you should read the question carefully
                - after deciding, enter the answer option key you have choosen (a, b, c, or d))
                - if right answer, you will be upgraded to next question
                if wrong answer, the quiz will be failed and u will have to start it all over again!
              INFO: If anytime you want to exit the quiz, u can type 'quit' or 'exit'
                Thanks and Good Luck!

                The Quiz started ...
                """)

    def answer_right(self): #we need to handle the max_level condition, what if level == 15??
        """method handle the right answer from the player"""
        if self.level > 0 and self.level <= MAX_LEVEL - 1:
            self.level += 1
        else:
            self.level = MAX_LEVEL
        print(f"""
              Congratulations! This is the correct answer and you are moving to next level, level: {self.level}
              """)
        return self.level

    def answer_wrong(self):
        """method handle the wrong answer from the player"""
        print(f"""
              Oops!! Wrong answer! Thanks for your time taking this quiz.
              You have answered {self.level - 1} questions out of 15!
              Don't lose hope! You can try again later!
              Bye!
              """)

    def won(self):
        """method handles when the player passes max_level"""
        if self.level == MAX_LEVEL and self.answer_right():
            print(f"""
                  Hoorraaay!, you have passed the last level in the quiz! level {self.level} .
                  U really know alot about ISLAM but we encourage to deep dive more into it!
                  Have great one ahead! Bye!
                  """)

    def end_quiz(self):
        """method handles when the player wants to end the quiz"""
        print(f"""
              Hey {self.name}, This is a confirmation that you want to leave the quiz, all your progress, will be deleted!
              """)
        player_confirmation = input("Enter 'yes' or 'no': ")
        if player_confirmation.lower() == 'yes' or player_confirmation.lower() == 'y':
            print("The quiz will be closed, See u later, Bye!")
        else:
            print(f"The quiz continues, you are now in level {self.level}")
        return player_confirmation
