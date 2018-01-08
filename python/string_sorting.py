# Can be done this way but innefficient
# s = 'cba'
# mylist = list(s)
# mylist.sort()
# ''.join(mylist)
# print(mylist)

# This is more efficient to write
# s = ''.join(sorted(s))
# print(s)

# Same operation but made into a function
def strsort(s):
  return ''.join(sorted(s))

print(strsort('cba'))
