#Make a function that adds the numbers from 1-255 into a list. Then print the list.

my_list = []
def my_func():
  for x in range(0, 256):
    my_list.insert(0, x)
my_func()
print(my_list)
