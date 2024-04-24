'''Write a function to convert camel case string to snake case string.
'''
def camel_to_snake(text):
    import re
    str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
'''
Standard answer: 
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()
'''
assert camel_to_snake('PythonProgram')==('python_program')
assert camel_to_snake('pythonLanguage')==('python_language')
assert camel_to_snake('ProgrammingLanguage')==('programming_language')
