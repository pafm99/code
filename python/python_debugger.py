# using python debugger

my_list = [ 5, 2, 1, True, "abcde", 3, False, 4]

import pbd; pdb.set_trace() # instead of importing at the top you will likely use pdb like this. 
#This is the only time you will use a semicolon in python

del my_list[3] # [ 5, 2, 1, "abcde", 3, False, 4]
del my_list[3] # [ 5, 2, 1, 3, False, 4]
del my_list[4] # [ 5, 2, 1, 3, 4]
print(my_list)