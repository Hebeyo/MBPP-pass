'''Write a python function to check if the string is a concatenation of another string.
'''
def check_Concat(str1,str2):
    if len(str1) % len(str2) != 0:
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i % len(str2)]:
            return False
    return True
'''
Standard answer: 
def check_Concat(str1,str2):
    N = len(str1)
    M = len(str2)
    if (N % M != 0):
        return False
    for i in range(N):
        if (str1[i] != str2[i % M]):
            return False         
    return True
'''
assert check_Concat("abcabcabc","abc") == True
assert check_Concat("abcab","abc") == False
assert check_Concat("aba","ab") == False
