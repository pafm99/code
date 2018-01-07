import random

x = random.randint(0,10)
print('Randomly chose number is {}'.format(x))
# in Python 2.7 you would use raw_input
user_guess = int(input("Enter a number: "))

if user_guess == x:
    print("You guessed correctly!")
elif user_guess < x:
    print("Too Low!")
elif user_guess > x:
    print("Too High!")
else:
    print("You should never see this!")
