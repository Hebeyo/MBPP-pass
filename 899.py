'''Write a python function to check whether an array can be sorted or not by picking only the corner elements.
'''
def check(arr,n):
    g = 0
    for i in range(1,n):
        if arr[i] - arr[i - 1] > 0 and g == 1:
            return False
        if arr[i] - arr[i] < 0:
            g = 1
    return True
'''
Standard answer: 
def check(arr,n): 
    g = 0 
    for i in range(1,n): 
        if (arr[i] - arr[i - 1] > 0 and g == 1): 
            return False
        if (arr[i] - arr[i] < 0): 
            g = 1
    return True
'''
assert check([3,2,1,2,3,4],6) == True
assert check([2,1,4,5,1],5) == True
assert check([1,2,2,1,2,3],6) == True
