import datetime
import random

from questions import Add, multiply

class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # Generate 10 random questions with numbers from 1 to 10
        # Add these questions into self.questions

    def take_quiz(self):
        # Log the Start Time
        # Ask all of the questions
        # Log if they got the question right
        # Log the end time
        # show a summary

    def ask(self, question):
        # log the start time
        # capture the answer
        # check the answer
        # log the end time
        # if the answer is right send back true
        # otherwise, send back false
        # send back the elapsed time

    def total_correct(self):
        # return the total # of correct answers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total

    def summary(self):
        # print how many they got right and the total like 5/10
        print("You got {} out of {} right".format(self.total_correct(), len(self.questions()))
        # print the total time for the quiz like 30 seconds!
        print("It took you {} second total".format((self.end_time-self.start_time).seconds))




