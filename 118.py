'''[link text](https:// [link text](https:// [link text](https://)))write a function to convert a string to a list.
'''
def string_to_list(string):
    lst = list(string.split(" "))
    return lst
'''
Standard answer: 
def string_to_list(string): 
    lst = list(string.split(" ")) 
    return lst
'''
assert string_to_list("python programming")==['python','programming']
assert string_to_list("lists tuples strings")==['lists','tuples','strings']
assert string_to_list("write a program")==['write','a','program']
