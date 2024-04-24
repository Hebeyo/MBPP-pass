'''Write a python function to count lower case letters in a given string.
'''
def lower_ctr(str):
    return sum(1 for c in str if c.islower())
'''
Standard answer: 
def lower_ctr(str):
      lower_ctr= 0
      for i in range(len(str)):
          if str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1     
      return  lower_ctr
'''
assert lower_ctr('abc') == 3
assert lower_ctr('string') == 6
assert lower_ctr('Python') == 5
