'''Write a function that matches a string that has an a followed by two to three 'b'.
'''
def text_match_two_three(text):
        import re
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
Standard answer: 
import re
def text_match_two_three(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_match_two_three("ac")==('Not matched!')
assert text_match_two_three("dc")==('Not matched!')
assert text_match_two_three("abbbba")==('Found a match!')
