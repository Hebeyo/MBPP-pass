'''Write a python function to check whether the given string is a binary string or not.
'''
def check(string) :
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        return ("Yes") 
    else : 
        return ("No")
'''
Standard answer: 
def check(string) :
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        return ("Yes") 
    else : 
        return ("No") 
'''
assert check("01010101010") == "Yes"
assert check("name0") == "No"
assert check("101") == "Yes"
