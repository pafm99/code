# Sum anything. Two different ways to implement

# def mysum(*args):
#   if not args:
#     return args
#   output = args[0]
#   for item in args[1:]:
#     output += item
#   return output
  
def mysum(*args):
  if not args:
    return args
  output = type(args[0])()
  for item in args:
    output += item
  return output
  
print(mysum(list('abc'), list('def')))
