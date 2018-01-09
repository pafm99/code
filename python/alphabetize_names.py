people =[{'first': 'barack', 'last': 'obama', 'email': 'president@example.com'}, 
        {'first': 'russel', 'last': 'simmons', 'email': 'russel@example.com'},
        {'first': 'paul', 'last': 'franco', 'email': 'paul@example.com'},
        {'first': 'jesus', 'last': 'ochoa', 'email': 'jesus@example.com'}]


for person in sorted(people, key=lambda p: p['last']):
  print("{last}, {first}: {email}".format(**person))
  
# prints:
# franco, paul: paul@example.com
# obama, barack: president@example.com
# ochoa, jesus: jesus@example.com
# simmons, russel: russel@example.com
