'''Write a function to find length of the string.
'''
def string_length(str1):
    return len(str1)
'''
Standard answer: 
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
'''
assert string_length('python')==6
assert string_length('program')==7
assert string_length('language')==8
