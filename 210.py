'''Write a function to check that the given string contains only a certain set of characters(in this case a-z, a-z and 0-9) by using regex.
'''
def is_allowed_specific_char(string):
    import re
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)
'''
Standard answer: 
import re
def is_allowed_specific_char(string):
    get_char = re.compile(r'[^a-zA-Z0-9.]')
    string = get_char.search(string)
    return not bool(string)
'''
assert is_allowed_specific_char("ABCDEFabcdef123450") == True
assert is_allowed_specific_char("*&%@#!}{") == False
assert is_allowed_specific_char("HELLOhowareyou98765") == True
