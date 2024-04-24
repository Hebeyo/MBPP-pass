'''Write a function to count total characters in a string.
'''
def count_charac(str1):
 total = 0
 for i in str1:
    total = total + 1
 return total
'''
Standard answer: 
def count_charac(str1):
 total = 0
 for i in str1:
    total = total + 1
 return total
'''
assert count_charac("python programming")==18
assert count_charac("language")==8
assert count_charac("words")==5
