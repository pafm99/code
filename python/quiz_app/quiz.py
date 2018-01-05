import datetime
import random

from questions import Add, Multiply

class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # Generate 10 random questions with numbers from 1 to 10
        question_types = (Add, Multiply)
        for _ in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            question = random.choice(question_types)(num1,num2)
            self.questions.append(question)
        # Add these questions into self.questions
    def take_quiz(self):
        # Log the Start Time
        self.start_time = datetime.datetime.now()       
        # Ask all of the questions
        for question in self.questions:
            self.answers.append(self.ask(question))
        else:
            self.end_time = datetime.datetime.now()
        # Log if they got the question right
        # Log the end time
        # show a summary
        return self.summary()

    def ask(self, question):
        correct = False
        # log the start time
        question_start = datetime.datetime.now()
        # capture the answer
        answer = input(question.text + ' = ')
        # check the answer
        if answer == str(question.answer):
            correct = True
        # log the end time
        question_end = datetime.datetime.now()
        # if the answer is right send back true
        # otherwise, send back false
        # send back the elapsed time
        return correct, question_end - question_start
    def total_correct(self):
        # return the total # of correct answers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many they got right and the total like 5/10
        print("You got {} out of {} right".format(self.total_correct(), len(self.questions)))
        # print the total time for the quiz like 30 seconds!
        print("It took you {} seconds total".format((self.end_time-self.start_time).seconds))

Quiz().take_quiz()


