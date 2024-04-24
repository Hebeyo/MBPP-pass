'''Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
'''
def text_starta_endb(text):
  if text[0] == 'a' and text[-1] == 'b':
    return 'Found a match!'
  else:
    return 'Not matched!'
'''
Standard answer: 
import re
def text_starta_endb(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_starta_endb("aabbbb")==('Found a match!')
assert text_starta_endb("aabAbbbc")==('Not matched!')
assert text_starta_endb("accddbbjjj")==('Not matched!')
