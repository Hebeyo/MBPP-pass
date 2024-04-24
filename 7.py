'''Write a function to find all words which are at least 4 characters long in a string by using regex.
'''
def find_char_long(text):
  import re
  return (re.findall(r"\b\w{4,}\b", text))
'''
Standard answer: 
import re
def find_char_long(text):
  return (re.findall(r"\b\w{4,}\b", text))
'''
assert find_char_long('Please move back to stream') == ['Please', 'move', 'back', 'stream']
assert find_char_long('Jing Eco and Tech') == ['Jing', 'Tech']
assert find_char_long('Jhingai wulu road Zone 3') == ['Jhingai', 'wulu', 'road', 'Zone']
