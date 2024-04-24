'''Write a function to search a literals string in a string and also find the location within the original string where the pattern occurs by using regex.
'''
def find_literals(text, pattern):
  import re
  match = re.search(pattern, text)
  s = match.start()
  e = match.end()
  return (match.re.pattern, s, e)
'''
Standard answer: 
import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
def find_literals(text, pattern):
  match = re.search(pattern, text)
  s = match.start()
  e = match.end()
  return (match.re.pattern, s, e)
'''
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
assert find_literals('Its been a very crazy procedure right', 'crazy') == ('crazy', 16, 21)
assert find_literals('Hardest choices required strongest will', 'will') == ('will', 35, 39)
