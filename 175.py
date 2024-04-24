'''Write a function to verify validity of a string of parentheses.
'''
def is_valid_parenthese(str1):
  stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
  for parenthese in str1:
    if parenthese in pchar:
      stack.append(parenthese)
    elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
      return False
  return len(stack) == 0
'''
Standard answer: 
def is_valid_parenthese( str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
'''
assert is_valid_parenthese("(){}[]")==True
assert is_valid_parenthese("()[{)}")==False
assert is_valid_parenthese("()")==True
