'''Write a function to split a string at uppercase letters.
'''
def split_upperstring(text):
    result = ''
    for i in text:
        if i.isupper():
            result += ' ' + i
        else:
            result += i
    return result.split()
'''
Standard answer: 
import re
def split_upperstring(text):
 return (re.findall('[A-Z][^A-Z]*', text))
'''
assert split_upperstring("PythonProgramLanguage")==['Python','Program','Language']
assert split_upperstring("PythonProgram")==['Python','Program']
assert split_upperstring("ProgrammingLanguage")==['Programming','Language']
