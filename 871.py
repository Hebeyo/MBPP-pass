'''Write a python function to check whether the given strings are rotations of each other or not.
'''
def are_Rotations(string1,string2): 
    size1 = len(string1) 
    size2 = len(string2) 
    temp = '' 
    if size1 != size2: 
        return False
    temp = string1 + string1 
    if (temp.count(string2)> 0): 
        return True
    else: 
        return False
'''
Standard answer: 
def are_Rotations(string1,string2): 
    size1 = len(string1) 
    size2 = len(string2) 
    temp = '' 
    if size1 != size2: 
        return False
    temp = string1 + string1 
    if (temp.count(string2)> 0): 
        return True
    else: 
        return False
'''
assert are_Rotations("abc","cba") == False
assert are_Rotations("abcd","cdba") == False
assert are_Rotations("abacd","cdaba") == True
