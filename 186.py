'''Write a function to search some literals strings in a string by using regex.
'''
def check_literals(text, patterns):
  for pattern in patterns:
    if pattern in text:
      return ('Matched!')
    else:
      return ('Not Matched!')
'''
Standard answer: 
import re
def check_literals(text, patterns):
  for pattern in patterns:
    if re.search(pattern,  text):
        return ('Matched!')
    else:
        return ('Not Matched!')
'''
assert check_literals('The quick brown fox jumps over the lazy dog.',['fox']) == 'Matched!'
assert check_literals('The quick brown fox jumps over the lazy dog.',['horse']) == 'Not Matched!'
assert check_literals('The quick brown fox jumps over the lazy dog.',['lazy']) == 'Matched!'
