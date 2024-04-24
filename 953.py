'''Write a python function to find the minimun number of subsets with distinct elements.
'''
def subset(ar, n): 
    res = 0
    ar.sort() 
    for i in range(0, n) : 
        count = 1
        for i in range(n - 1): 
            if ar[i] == ar[i + 1]: 
                count+=1
            else: 
                break 
        res = max(res, count)  
    return res
'''
Standard answer: 
def subset(ar, n): 
    res = 0
    ar.sort() 
    for i in range(0, n) : 
        count = 1
        for i in range(n - 1): 
            if ar[i] == ar[i + 1]: 
                count+=1
            else: 
                break 
        res = max(res, count)  
    return res 
'''
assert subset([1, 2, 3, 4],4) == 1
assert subset([5, 6, 9, 3, 4, 3, 4],7) == 2
assert subset([1, 2, 3 ],3) == 1
