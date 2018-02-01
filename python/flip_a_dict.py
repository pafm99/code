# Flip a Dict

x = {'a': 1, 'b': 2, 'c': 3}

f = {value : key
      for key, value in x.items()}
print(f)

# To flip a dict this way the keys must be unique, so if 2 keys have the same value then the dictionary will be shortened to the number of unique values. Also, the keys must be hashable.
