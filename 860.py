'''Write a function to check whether the given string is ending with only alphanumeric characters or not using regex.
'''
def check_alphanumeric(string):
  if string[-1].isalnum():
    return "Accept"
  else:
    return "Discard"
'''
Standard answer: 
import re 
regex = '[a-zA-z0-9]$'
def check_alphanumeric(string): 
	if(re.search(regex, string)): 
		return ("Accept") 
	else: 
		return ("Discard") 
'''
assert check_alphanumeric("dawood@") == 'Discard'
assert check_alphanumeric("skdmsam326") == 'Accept'
assert check_alphanumeric("cooltricks@") == 'Discard'
