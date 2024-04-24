'''Write a function to check if the string is a valid email address or not using regex.
'''
def check_email(email):
    import re
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):
        return ("Valid Email")
    else:
        return ("Invalid Email")
'''
Standard answer: 
import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check_email(email): 
	if(re.search(regex,email)): 
		return ("Valid Email") 
	else: 
		return ("Invalid Email") 
'''
assert check_email("ankitrai326@gmail.com") == 'Valid Email'
assert check_email("my.ownsite@ourearth.org") == 'Valid Email'
assert check_email("ankitaoie326.com") == 'Invalid Email'
