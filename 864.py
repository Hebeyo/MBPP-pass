'''Write a function to find palindromes in a given list of strings using lambda function.
'''
def palindrome_lambda(texts):
  result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
  return result
'''
Standard answer: 
def palindrome_lambda(texts):
  result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
  return result
'''
assert palindrome_lambda(["php", "res", "Python", "abcd", "Java", "aaa"])==['php', 'aaa']
assert palindrome_lambda(["abcd", "Python", "abba", "aba"])==['abba', 'aba']
assert palindrome_lambda(["abcd", "abbccbba", "abba", "aba"])==['abbccbba', 'abba', 'aba']
