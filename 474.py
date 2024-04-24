'''Write a function to replace characters in a string.
'''
def replace_char(str1,ch,newch):
    str2 = ""
    for i in str1:
        if i == ch:
            str2 += newch
        else:
            str2 += i
    return str2
'''
Standard answer: 
def replace_char(str1,ch,newch):
 str2 = str1.replace(ch, newch)
 return str2
'''
assert replace_char("polygon",'y','l')==("pollgon")
assert replace_char("character",'c','a')==("aharaater")
assert replace_char("python",'l','a')==("python")
