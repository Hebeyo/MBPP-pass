'''Write a function to find sequences of one upper case letter followed by lower case letters in the given string by using regex.
'''
import re
def match(text):
		pattern = '[A-Z]+[a-z]+$'
		if re.search(pattern, text):
				return('Yes')
		else:
				return('No')
'''
Standard answer: 
import re 
def match(text): 
		pattern = '[A-Z]+[a-z]+$'
		if re.search(pattern, text): 
				return('Yes') 
		else: 
				return('No') 
'''
assert match("Geeks") == 'Yes'
assert match("geeksforGeeks") == 'Yes'
assert match("geeks") == 'No'
