'''Write a function to check whether the given string is starting with a vowel or not using regex.
'''
def check_str(string):
    if string[0] in 'aeiouAEIOU':
        return 'Valid'
    else:
        return 'Invalid'
'''
Standard answer: 
import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	if(re.search(regex, string)): 
		return ("Valid") 
	else: 
		return ("Invalid") 
'''
assert check_str("annie") == 'Valid'
assert check_str("dawood") == 'Invalid'
assert check_str("Else") == 'Valid'
