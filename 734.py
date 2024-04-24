'''Write a python function to find sum of products of all possible subarrays.
'''
def sum_Of_Subarray_Prod(arr,n):
    ans = 0
    res = 0
    i = n - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
'''
Standard answer: 
def sum_Of_Subarray_Prod(arr,n):
    ans = 0
    res = 0
    i = n - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
'''
assert sum_Of_Subarray_Prod([1,2,3],3) == 20
assert sum_Of_Subarray_Prod([1,2],2) == 5
assert sum_Of_Subarray_Prod([1,2,3,4],4) == 84
