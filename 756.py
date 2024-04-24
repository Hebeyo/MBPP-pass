'''Write a function that matches a string that has an a followed by zero or one 'b'.
'''
import re
def text_match_zero_one(text):
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
Standard answer: 
import re
def text_match_zero_one(text):
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_match_zero_one("ac")==('Found a match!')
assert text_match_zero_one("dc")==('Not matched!')
assert text_match_zero_one("abbbba")==('Found a match!')
