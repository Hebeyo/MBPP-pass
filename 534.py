'''Write a function to search a literals string in a string and also find the location within the original string where the pattern occurs.
'''
def search_literal(pattern,text):
    s = text.find(pattern)
    e = s + len(pattern)
    return (s, e)
'''
Standard answer: 
import re
def search_literal(pattern,text):
 match = re.search(pattern, text)
 s = match.start()
 e = match.end()
 return (s, e)
'''
assert search_literal('python','python programming language')==(0,6)
assert search_literal('programming','python programming language')==(7,18)
assert search_literal('language','python programming language')==(19,27)
