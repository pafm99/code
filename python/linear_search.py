# Linear Search
   
list_of_elements = [ 1, 7, 5, 9, 2, 4]

search = int(input("Enter a number you would like to search: "))    # ask for a number
for i in range(len(list_of_elements)): # repeat for each item in list
  if search==list_of_elements[i]: #if item at position i is search time
    print(str(search) + " found at position " + str(i)) #report find
