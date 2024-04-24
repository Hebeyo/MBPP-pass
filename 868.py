'''Write a python function to find the length of the last word in a given string.
'''
def length_Of_Last_Word(a): 
    l = 0
    x = a.strip() 
    for i in range(len(x)): 
        if x[i] == " ": 
            l = 0
        else: 
            l += 1
    return l
'''
Standard answer: 
def length_Of_Last_Word(a): 
    l = 0
    x = a.strip() 
    for i in range(len(x)): 
        if x[i] == " ": 
            l = 0
        else: 
            l += 1
    return l 
'''
assert length_Of_Last_Word("python language") == 8
assert length_Of_Last_Word("PHP") == 3
assert length_Of_Last_Word("") == 0
