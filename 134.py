'''Write a python function to check whether the last element of given array is even or odd after performing an operation p times.
'''
def check_last (arr,n,p):
    _sum = 0
    for i in range(n):
        _sum = _sum + arr[i]
    if p == 1:
        if _sum % 2 == 0:
            return "ODD"
        else:
            return "EVEN"
    return "EVEN"
'''
Standard answer: 
def check_last (arr,n,p): 
    _sum = 0
    for i in range(n): 
        _sum = _sum + arr[i] 
    if p == 1: 
        if _sum % 2 == 0: 
            return "ODD"
        else: 
            return "EVEN"
    return "EVEN"
      
'''
assert check_last([5,7,10],3,1) == "ODD"
assert check_last([2,3],2,3) == "EVEN"
assert check_last([1,2,3],3,1) == "ODD"
