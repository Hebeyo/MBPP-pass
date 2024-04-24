'''Write a python function to remove all occurrences of a character in a given string.
'''
def remove_Char(s,c) :  
    counts = s.count(c) 
    s = list(s) 
    while counts :  
        s.remove(c) 
        counts -= 1 
    s = '' . join(s)   
    return (s)
'''
Standard answer: 
def remove_Char(s,c) :  
    counts = s.count(c) 
    s = list(s) 
    while counts :  
        s.remove(c) 
        counts -= 1 
    s = '' . join(s)   
    return (s) 
'''
assert remove_Char("aba",'a') == "b"
assert remove_Char("toggle",'g') == "tole"
assert remove_Char("aabbc",'b') == "aac"
