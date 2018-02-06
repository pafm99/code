# Create a program that reads some files and returns the longest word in those files
import os
dirname = input("Enter a dirname: ")
def longest_word(filename):
  return max(open(dirname + '/' + filename).read().split(), key=len)

  
print({dirname + "/" + filename: longest_word(filename)
      for filename in os.listdir(dirname)})
