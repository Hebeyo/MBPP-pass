'''Write a python function to add a minimum number such that the sum of array becomes even.
'''
def min_Num(arr,n): 
    odd = 0
    for i in range(n): 
        if (arr[i] % 2): 
            odd += 1 
    if (odd % 2): 
        return 1
    return 2
'''
Standard answer: 
def min_Num(arr,n):  
    odd = 0
    for i in range(n): 
        if (arr[i] % 2): 
            odd += 1 
    if (odd % 2): 
        return 1
    return 2
'''
assert min_Num([1,2,3,4,5,6,7,8,9],9) == 1
assert min_Num([1,2,3,4,5,6,7,8],8) == 2
assert min_Num([1,2,3],3) == 2
