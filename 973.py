'''Write a python function to left rotate the string.
'''
def left_rotate(s,d):
    tmp = s[d : ] + s[0 : d]
    return tmp
'''
Standard answer: 
def left_rotate(s,d):
    tmp = s[d : ] + s[0 : d]
    return tmp  
'''
assert left_rotate("python",2) == "thonpy"   
assert left_rotate("bigdata",3 ) == "databig" 
assert left_rotate("hadoop",1 ) == "adooph" 
