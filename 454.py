'''Write a function that matches a word containing 'z'.
'''
def text_match_wordz(text):
  if 'z' in text:
      return 'Found a match!'
  else:
      return('Not matched!')
'''
Standard answer: 
import re
def text_match_wordz(text):
        patterns = '\w*z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_match_wordz("pythonz.")==('Found a match!')
assert text_match_wordz("xyz.")==('Found a match!')
assert text_match_wordz("  lang  .")==('Not matched!')
