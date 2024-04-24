'''Write a function to split the given string at uppercase letters by using regex.
'''
def split_list(text):
  res = []
  temp = ''
  for i in range(len(text)):
    if text[i].isupper():
      res.append(temp)
      temp = ''
    temp += text[i]
  res.append(temp)
  res.remove('')
  return res
'''
Standard answer: 
import re
def split_list(text):
  return (re.findall('[A-Z][^A-Z]*', text))
'''
assert split_list("LearnToBuildAnythingWithGoogle") == ['Learn', 'To', 'Build', 'Anything', 'With', 'Google']
assert split_list("ApmlifyingTheBlack+DeveloperCommunity") == ['Apmlifying', 'The', 'Black+', 'Developer', 'Community']
assert split_list("UpdateInTheGoEcoSystem") == ['Update', 'In', 'The', 'Go', 'Eco', 'System']
