'''Write a python function to find the first missing positive number.
'''
def first_Missing_Positive(arr,n):
    ptr = 0
    for i in range(n):
        if arr[i] == 1:
            ptr = 1
            break
    if ptr == 0:
        return(1)
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
    for i in range(n):
        arr[(arr[i] - 1) % n] += n
    for i in range(n):
        if arr[i] <= n:
            return(i + 1)
    return(n + 1)
'''
Standard answer: 
def first_Missing_Positive(arr,n): 
    ptr = 0
    for i in range(n):
        if arr[i] == 1:
            ptr = 1
            break
    if ptr == 0:
        return(1)
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
    for i in range(n):
        arr[(arr[i] - 1) % n] += n
    for i in range(n):
        if arr[i] <= n:
            return(i + 1)
    return(n + 1)
'''
assert first_Missing_Positive([1,2,3,-1,5],5) == 4
assert first_Missing_Positive([0,-1,-2,1,5,8],6) == 2
assert first_Missing_Positive([0,1,2,5,-8],5) == 3
