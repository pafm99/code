#pyformat.info
people = [('Barack', 'Obama', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', "Xi", 10.603)]
#def by_last_name(t):
#  return t[1]
  
for person in sorted(people, key=lambda t: (t[1], t[0])):
  print('{1:10} {2:10} {2:5.2f}'.format(*person))
