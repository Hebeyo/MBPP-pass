'''Write a python function to sort the given string.
'''
def sort_String(str) : 
    str = ''.join(sorted(str)) 
    return (str)
'''
Standard answer: 
def sort_String(str) : 
    str = ''.join(sorted(str)) 
    return (str) 
'''
assert sort_String("cba") == "abc"
assert sort_String("data") == "aadt"
assert sort_String("zxy") == "xyz"
