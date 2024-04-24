'''Write a python function to find minimum number swaps required to make two binary strings equal.
'''
def min_Swaps(s1,s2) : 
    c0 = 0
    c1 = 0
    for i in range(len(s1)) : 
        if (s1[i] == '0' and s2[i] == '1') : 
            c0 += 1
        elif (s1[i] == '1' and s2[i] == '0') : 
            c1 += 1
    result = c0 // 2 + c1 // 2
    if (c0 % 2 == 0 and c1 % 2 == 0) : 
        return result
    elif ((c0 + c1) % 2 == 0) : 
        return result + 2
    else : 
        return -1
'''
Standard answer: 
def min_Swaps(s1,s2) :  
    c0 = 0; c1 = 0;  
    for i in range(len(s1)) :  
        if (s1[i] == '0' and s2[i] == '1') : 
            c0 += 1;    
        elif (s1[i] == '1' and s2[i] == '0') : 
            c1 += 1;  
    result = c0 // 2 + c1 // 2;  
    if (c0 % 2 == 0 and c1 % 2 == 0) : 
        return result;  
    elif ((c0 + c1) % 2 == 0) : 
        return result + 2;  
    else : 
        return -1;  
'''
assert min_Swaps("0011","1111") == 1
assert min_Swaps("00011","01001") == 2
assert min_Swaps("111","111") == 0
