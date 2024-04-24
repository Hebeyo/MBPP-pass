'''Write a function to replace blank spaces with any character in a string.
'''
def replace_blank(str1,char):
    str2 = ""
    for i in str1:
        if i == " ":
            str2 = str2 + char
        else:
            str2 = str2 + i
    return str2
'''
Standard answer: 
def replace_blank(str1,char):
 str2 = str1.replace(' ', char)
 return str2
'''
assert replace_blank("hello people",'@')==("hello@people")
assert replace_blank("python program language",'$')==("python$program$language")
assert replace_blank("blank space","-")==("blank-space")
