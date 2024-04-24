'''Write a python function to find the first position of an element in a sorted array.
'''
def first(arr,x,n):
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid - 1
    return res
'''
Standard answer: 
def first(arr,x,n): 
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid - 1
    return res
'''
assert first([1,2,3,4,5,6,6],6,6) == 5
assert first([1,2,2,2,3,2,2,4,2],2,9) == 1
assert first([1,2,3],1,3) == 0
