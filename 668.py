'''Write a python function to replace multiple occurence of character by single.
'''
def replace(string, char):
    str = list(string)
    i = 0
    while(i < len(str)):
        if(str[i] == char):
            j = i + 1
            while(j < len(str) and str[j] == char):
                j = j + 1
            if(j - i > 1):
                del str[i + 1:j]
        i = i + 1
    return "".join(str)
'''
Standard answer: 
import re 
def replace(string, char): 
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string 
'''
assert replace('peep','e') == 'pep'
assert replace('Greek','e') == 'Grek'
assert replace('Moon','o') == 'Mon'
