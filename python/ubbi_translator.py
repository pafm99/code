# Everytime you have a vowel you have to add "ub" ex: apple => ubapplube

word = input("Enter a word: ")
output = []
for letter in word:
  if letter in 'aeiou':
    output.append('ub' + letter)
  else:
    output.append(letter)
print(''.join(output))
