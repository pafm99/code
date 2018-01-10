# The Python way
# Suppose you had a list of numbers, and you wanted to add 5 to every item in the list. Without NumPy, you might do something like this:

values = [1,2,3,4,5]
for i in range(len(values)):
    values[i] += 5

# now values holds [6,7,8,9,10]

# That makes sense, but it's a lot of code to write and it runs slowly because it's pure Python.

# Note: Just in case you aren't used to using operators like +=, that just means "add these two items and then store the result in the left item." It is a more succinct way of writing values[i] = values[i] + 5. The code you see in these examples makes use of such operators whenever possible.

# The NumPy way
# In NumPy, we could do the following:

values = [1,2,3,4,5]
values = np.array(values) + 5

# now values is an ndarray that holds [6,7,8,9,10]
