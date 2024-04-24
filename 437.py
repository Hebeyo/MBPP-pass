'''Write a function to remove odd characters in a string.
'''
def remove_odd(str1):
    str2 = ''
    for i in range(1, len(str1) + 1):
        if(i % 2 == 0):
            str2 = str2 + str1[i - 1]
    return str2
'''
Standard answer: 
def remove_odd(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
'''
assert remove_odd("python")==("yhn")
assert remove_odd("program")==("rga")
assert remove_odd("language")==("agae")
