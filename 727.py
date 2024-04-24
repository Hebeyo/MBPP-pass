'''Write a function to remove all characters except letters and numbers using regex
'''
def remove_char(S):
  import re 
  result = re.sub('[\W_]+', '', S) 
  return result
'''
Standard answer: 
import re 
def remove_char(S):
  result = re.sub('[\W_]+', '', S) 
  return result
'''
assert remove_char("123abcjw:, .@! eiw") == '123abcjweiw'
assert remove_char("Hello1234:, ! Howare33u") == 'Hello1234Howare33u'
assert remove_char("Cool543Triks@:, Make@987Trips") == 'Cool543TriksMake987Trips' 
