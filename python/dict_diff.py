# Take 2 dictionaries and find out what are the differences between them

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 4}

def dict_diff(d1, d2):
  output = {}
  all_keys = set(d1.keys())
  all_keys.update(d2.keys())
  
  for key in all_keys:
    v1 = d1.get(key)
    v2 = d2.get(key)
    if v1 != v2:
      output[key] = [v1, v2]
  print(output)
  return output


dict_diff(dict1,dict1) # Expected Result is = {}
dict_diff(dict1,dict2) # Expected Results is = {'c': [3,4]}
