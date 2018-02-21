# Given a string, return the string without spaces. Do not use pre-made string functions

my_string = "Lets practice algorithms"

def removeSpaces(str):
  new_str = ""
  for i in range(len(str)):
    if (str[i] != " "):
      new_str += str[i]
  return new_str
  

print(removeSpaces(my_string))
