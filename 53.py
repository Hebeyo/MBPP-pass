'''Write a python function to check whether the first and last characters of a given string are equal or not.
'''
def check_Equality(str):
  if (str[0] == str[-1]):  
    return ("Equal") 
  else:  
    return ("Not Equal")
'''
Standard answer: 
def check_Equality(str):
  if (str[0] == str[-1]):  
    return ("Equal") 
  else:  
    return ("Not Equal") 
'''
assert check_Equality("abcda") == "Equal"
assert check_Equality("ab") == "Not Equal"
assert check_Equality("mad") == "Not Equal"
