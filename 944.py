'''Write a function to separate and print the numbers and their position of a given string.
'''
def num_position(text):
  for i in range(len(text)):
    if text[i].isdigit():
      return i
  return -1
'''
Standard answer: 
import re
def num_position(text):
 for m in re.finditer("\d+", text):
    return m.start()
'''
assert num_position("there are 70 flats in this apartment")==10
assert num_position("every adult have 32 teeth")==17
assert num_position("isha has 79 chocolates in her bag")==9
