'''Write a function to remove lowercase substrings from a given string.
'''
import re
def remove_lowercase(str1):
 remove_lower = lambda text: re.sub('[a-z]', '', text)
 result =  remove_lower(str1)
 return result
'''
Standard answer: 
import re
def remove_lowercase(str1):
 remove_lower = lambda text: re.sub('[a-z]', '', text)
 result =  remove_lower(str1)
 return result
'''
assert remove_lowercase("PYTHon")==('PYTH')
assert remove_lowercase("FInD")==('FID')
assert remove_lowercase("STRinG")==('STRG')
