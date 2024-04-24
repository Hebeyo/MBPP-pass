'''Write a python function to find the first non-repeated character in a given string.
'''
def first_non_repeating_character(str1):
  for i in range(len(str1)):
    found = False
    for j in range(len(str1)):
      if i != j and str1[i] == str1[j]:
        found = True
        break
    if not found:
      return str1[i]
  return None
'''
Standard answer: 
def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None
'''
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abc") == "a"
assert first_non_repeating_character("ababc") == "c"
