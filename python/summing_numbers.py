# Built in sum function:
# sum([[1,2], [2,1]], []) 



#This is what is happening behing the scenes

# def mysum(items):
  # first_element_type = type(items[0])
  
  # if first_element_type == str:
  #   output = ''
  # elif first_element_type == list:
  #   output = []
  # elif first_element_type == int:
  #   output = 0
  # elif first_element_type == tuple:
  #   output = ()
    
  # for item in items:
  #   output += item
  # return output
  
  
# This is a more compact way of writing the code above  
def mysum(items):
  #if not items handles if we get something that is empty
  if not items:
    return items
    
  output = type(items[0])()
  
  for item in items:
    output += item
  return output
  
#print(mysum(range(4)))
print(mysum([[1,2,3], [4,5,6]]))
print(mysum(((1,2,3), (4,5,6))))
print(sum([[1,2], [2,1]], []))
