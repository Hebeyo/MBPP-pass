'''Write a python function to count the number of substrings with same first and last characters.
'''
def count_Substring_With_Equal_Ends(s):
    result = 0
    n = len(s)
    for i in range(n):
        for j in range(1,n-i+1):
            if s[i] == s[i+j-1]:
                result += 1
    return result
'''
Standard answer: 
def check_Equality(s): 
    return (ord(s[0]) == ord(s[len(s) - 1])); 
def count_Substring_With_Equal_Ends(s): 
    result = 0; 
    n = len(s); 
    for i in range(n):
        for j in range(1,n-i+1): 
            if (check_Equality(s[i:i+j])): 
                result+=1; 
    return result; 
'''
assert count_Substring_With_Equal_Ends('aba') == 4
assert count_Substring_With_Equal_Ends('abcab') == 7
assert count_Substring_With_Equal_Ends('abc') == 3
