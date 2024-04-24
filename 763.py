'''Write a python function to find the minimum difference between any two elements in a given array.
'''
def find_Min_Diff(arr,n): 
    diff = 10**20 
    for i in range(n-1): 
        for j in range(i+1,n): 
            if abs(arr[i]-arr[j]) < diff: 
                diff = abs(arr[i] - arr[j])  
    return diff
'''
Standard answer: 
def find_Min_Diff(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
'''
assert find_Min_Diff((1,5,3,19,18,25),6) == 1
assert find_Min_Diff((4,3,2,6),4) == 1
assert find_Min_Diff((30,5,20,9),4) == 4
