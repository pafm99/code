import sys
import random

question = True

while question:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "exit":
        sys.exit()
    
    elif answers == 1:
        print("Everything for certain")
    
    elif answers == 2:
        print("Good possibilities")
    
    elif answers == 3:
        print("You may rely on it")
    
    elif answers == 4:
        print("Ask again later")
    
    elif answers == 5:
        print("Concentrate and ask again")
    
    elif answers == 6:
        print("Hell's No")
    
    elif answers == 7:
        print("My answer is no")
    
    elif answers == 8:
        print("My sources say no")
