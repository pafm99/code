#find the max number in a list of numbers
my_list = [3, 6, 1, 9, -7, 2, 0, 8, 4]
def find_max():
    max = 0
    for x in my_list:
        if x > max:
            max = x
    print(max)

#find the min in a list of numbers
def find_min():
    min = 0
    for x in my_list:
        if x < min:
            min = x
    print(min)

find_max()
find_min()