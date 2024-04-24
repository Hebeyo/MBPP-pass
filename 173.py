'''Write a function to remove everything except alphanumeric characters from a string.
'''
def remove_splchar(text):
  result = ''
  for char in text:
    if char.isalnum():
      result += char
  return result
'''
Standard answer: 
import re
def remove_splchar(text): 
 pattern = re.compile('[\W_]+')
 return (pattern.sub('', text))
'''
assert remove_splchar('python  @#&^%$*program123')==('pythonprogram123')
assert remove_splchar('python %^$@!^&*()  programming24%$^^()    language')==('pythonprogramming24language')
assert remove_splchar('python   ^%&^()(+_)(_^&67)                  program')==('python67program')
