'''Write a function to count alphabets,digits and special charactes in a given string.
'''
def count_alpha_dig_spl(string):
  alphabets=digits = special = 0
  for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
  return (alphabets,digits,special)
'''
Standard answer: 
def count_alpha_dig_spl(string):
  alphabets=digits = special = 0
  for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
  return (alphabets,digits,special)   
'''
assert count_alpha_dig_spl("abc!@#123")==(3,3,3)
assert count_alpha_dig_spl("dgsuy@#$%&1255")==(5,4,5)
assert count_alpha_dig_spl("fjdsif627348#%$^&")==(6,6,5)
