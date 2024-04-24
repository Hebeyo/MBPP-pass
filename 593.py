'''Write a function to remove leading zeroes from an ip address.
'''
def removezero_ip(ip):
    ip_split = ip.split('.')
    new_ip = []
    for i in ip_split:
        new_ip.append(str(int(i)))
    return '.'.join(new_ip)
'''
Standard answer: 
import re
def removezero_ip(ip):
 string = re.sub('\.[0]*', '.', ip)
 return string
'''
assert removezero_ip("216.08.094.196")==('216.8.94.196') 
assert removezero_ip("12.01.024")==('12.1.24') 
assert removezero_ip("216.08.094.0196")==('216.8.94.196') 
