'''Write a function to remove the parenthesis area in a string.
'''
def remove_parenthesis(items):
    for item in items:
        return item.split('(')[0].strip()
'''
Standard answer: 
import re
def remove_parenthesis(items):
 for item in items:
    return (re.sub(r" ?\([^)]+\)", "", item))
'''
assert remove_parenthesis(["python (chrome)"])==("python")
assert remove_parenthesis(["string(.abc)"])==("string")
assert remove_parenthesis(["alpha(num)"])==("alpha")
