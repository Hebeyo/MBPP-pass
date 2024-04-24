'''Write a function to check if a url is valid or not using regex.
'''
def is_valid_URL(str):
	import re
	regex = ("((http|https)://)(www.)?" +
			"[a-zA-Z0-9@:%._\\+~#?&//=]" +
			"{2,256}\\.[a-z]" +
			"{2,6}\\b([-a-zA-Z0-9@:%" +
			"._\\+~#?&//=]*)")
	p = re.compile(regex)
	if (str == None):
		return False
	if(re.search(p, str)):
		return True
	else:
		return False
'''
Standard answer: 
import re
def is_valid_URL(str):
	regex = ("((http|https)://)(www.)?" +
			"[a-zA-Z0-9@:%._\\+~#?&//=]" +
			"{2,256}\\.[a-z]" +
			"{2,6}\\b([-a-zA-Z0-9@:%" +
			"._\\+~#?&//=]*)")
	p = re.compile(regex)
	if (str == None):
		return False
	if(re.search(p, str)):
		return True
	else:
		return False
'''
assert is_valid_URL("https://www.google.com") == True
assert is_valid_URL("https:/www.gmail.com") == False
assert is_valid_URL("https:// www.redit.com") == False
