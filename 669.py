'''Write a function to check whether the given ip address is valid or not using regex.
'''
def check_IP(Ip):
	import re
	regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
				25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
				25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
				25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
	if(re.search(regex, Ip)):
		return ("Valid IP address")
	else:
		return ("Invalid IP address")
"""
Standard answer: 
import re 
regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
def check_IP(Ip): 
	if(re.search(regex, Ip)): 
		return ("Valid IP address") 
	else: 
		return ("Invalid IP address") 
"""

assert check_IP("192.168.0.1") == 'Valid IP address'
assert check_IP("110.234.52.124") == 'Valid IP address'
assert check_IP("366.1.2.2") == 'Invalid IP address'
