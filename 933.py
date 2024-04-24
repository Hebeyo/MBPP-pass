'''Write a function to convert camel case string to snake case string by using regex.
'''
import re
def camel_to_snake(text):
  str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
'''
Standard answer: 
import re
def camel_to_snake(text):
  str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
  return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
'''
assert camel_to_snake('GoogleAssistant') == 'google_assistant'
assert camel_to_snake('ChromeCast') == 'chrome_cast'
assert camel_to_snake('QuadCore') == 'quad_core'
