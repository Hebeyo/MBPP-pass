'''Write a function to replace maximum n occurrences of spaces, commas, or dots with a colon.
'''
def replace_max_specialchar(text,n):
    count = 0
    text = list(text)
    for i in range(len(text)):
        if (text[i] == ' ' or text[i] == ',' or text[i] == '.'):
            if (count < n):
                text[i] = ':'
                count += 1
            else:
                break
    return ''.join(text)
'''
Standard answer: 
import re
def replace_max_specialchar(text,n):
 return (re.sub("[ ,.]", ":", text, n))
'''
assert replace_max_specialchar('Python language, Programming language.',2)==('Python:language: Programming language.')
assert replace_max_specialchar('a b c,d e f',3)==('a:b:c:d e f')
assert replace_max_specialchar('ram reshma,ram rahim',1)==('ram:reshma,ram rahim')
