'''Write a function to check whether the given string starts and ends with the same character or not using regex.
'''
def check_char(string):
	import re
	regex = r'^[a-z]$|^([a-z]).*\1$'
	if(re.search(regex, string)):
		return "Valid"
	else:
		return "Invalid"
'''
Standard answer: 
import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
def check_char(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "Invalid" 
'''
assert check_char("abba") == "Valid"
assert check_char("a") == "Valid"
assert check_char("abcd") == "Invalid"
