'''Write a python function to convert a given string list to a tuple.
'''
def string_list_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result
'''
Standard answer: 
def string_list_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result
'''
assert string_list_to_tuple(("python 3.0")) == ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
assert string_list_to_tuple(("bigdata")) == ('b', 'i', 'g', 'd', 'a', 't', 'a')
assert string_list_to_tuple(("language")) == ('l', 'a', 'n', 'g', 'u', 'a', 'g','e')
