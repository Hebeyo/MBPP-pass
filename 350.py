'''Write a python function to minimize the length of the string by removing occurrence of only one character.
'''
def minimum_Length(s) : 
    maxOcc = 0
    n = len(s) 
    arr = [0]*26
    for i in range(n) : 
        arr[ord(s[i]) -ord('a')] += 1
    for i in range(26) : 
        if arr[i] > maxOcc : 
            maxOcc = arr[i] 
    return n - maxOcc
'''
Standard answer: 
def minimum_Length(s) : 
    maxOcc = 0
    n = len(s) 
    arr = [0]*26
    for i in range(n) : 
        arr[ord(s[i]) -ord('a')] += 1
    for i in range(26) : 
        if arr[i] > maxOcc : 
            maxOcc = arr[i] 
    return n - maxOcc 
'''
assert minimum_Length("mnm") == 1
assert minimum_Length("abcda") == 3
assert minimum_Length("abcb") == 2
