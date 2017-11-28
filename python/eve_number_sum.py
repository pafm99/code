# write a function that adds all of of the even numbers from 0 - 26

def my_func():
  my_sum = 0
  for x in range(0, 25):
    if x % 2 == 0:
      my_sum = my_sum + x
  print(my_sum)
my_func()