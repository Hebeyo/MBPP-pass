'''Write a function to find all anagrams of a string in a given list of strings using lambda function.
'''
def anagram_lambda(texts,str):
  result = list(filter(lambda x: (sorted(str) == sorted(x)), texts)) 
  return result
'''
Standard answer: 
from collections import Counter 
def anagram_lambda(texts,str):
  result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
  return result
'''
assert anagram_lambda(["bcda", "abce", "cbda", "cbea", "adcb"],"abcd")==['bcda', 'cbda', 'adcb']
assert anagram_lambda(["recitals"," python"], "articles" )==["recitals"]
assert anagram_lambda([" keep"," abcdef"," xyz"]," peek")==[" keep"]
