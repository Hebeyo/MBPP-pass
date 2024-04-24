'''Write a function to find out the second most repeated (or frequent) string in the given sequence.
'''
def second_frequent(input):
  dict = {}
  for i in input:
    if i in dict:
      dict[i] += 1
    else:
      dict[i] = 1
  max1 = max2 = 0
  for value in dict.values():
    if value > max1:
      max2 = max1
      max1 = value
    elif value > max2:
      max2 = value
  for key in dict:
    if dict[key] == max2:
      return key
  return "No second most frequent string"
'''
Standard answer: 
from collections import Counter 
	
def second_frequent(input): 
	dict = Counter(input) 
	value = sorted(dict.values(), reverse=True)  
	second_large = value[1] 
	for (key, val) in dict.items(): 
		if val == second_large: 
			return (key) 
'''
assert second_frequent(['aaa','bbb','ccc','bbb','aaa','aaa']) == 'bbb'
assert second_frequent(['abc','bcd','abc','bcd','bcd','bcd']) == 'abc'
assert second_frequent(['cdma','gsm','hspa','gsm','cdma','cdma']) == 'gsm'
