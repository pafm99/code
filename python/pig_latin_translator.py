# if first letter of the word is a vowel add "way" to the end of the word ex: air => airway
# if first letter of the word in not a vowel move the first letter of the word to the end then ad 'ay' ex: pizza => izzapay

word = input("Enter a word: ")

if word[0] in 'aeiou':
  print(word + 'way')
else:
  print(word[1:] + word[0] + 'ay')
