'''Write a python function to find the first repeated word in a given string.
'''
def first_repeated_word(str1):
  temp = set()
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.add(word)
  return 'None'
'''
Standard answer: 
def first_repeated_word(str1):
  temp = set()
  for word in str1.split():
    if word in temp:
      return word;
    else:
      temp.add(word)
  return 'None'
'''
assert first_repeated_word("ab ca bc ab") == "ab"
assert first_repeated_word("ab ca bc") == 'None'
assert first_repeated_word("ab ca bc ca ab bc") == "ca"
