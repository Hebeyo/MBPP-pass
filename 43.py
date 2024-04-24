'''Write a function to find sequences of lowercase letters joined with an underscore using regex.
'''
def text_match(text):
  import re
  patterns = '^[a-z]+_[a-z]+$'
  if re.search(patterns,  text):
    return ('Found a match!')
  else:
    return ('Not matched!')
'''
Standard answer: 
import re
def text_match(text):
  patterns = '^[a-z]+_[a-z]+$'
  if re.search(patterns,  text):
    return ('Found a match!')
  else:
    return ('Not matched!')
'''
assert text_match("aab_cbbbc") == 'Found a match!'
assert text_match("aab_Abbbc") == 'Not matched!'
assert text_match("Aaab_abbbc") == 'Not matched!'
assert text_match("aab-cbbbc") == 'Not matched!'
