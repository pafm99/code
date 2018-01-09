# word that has the most repeated letter in it from words
from collections import Counter


words = ['his', 'is', 'a', 'test', 'program', 'westwing']

word_counts = { word: max(Counter(word).items(), key=lambda pair: pair[1]) for word in words }
print(max(word_counts, key=lambda w: word_counts[w][1]))
# should give back the word test because t is the most repeated letter in the words
