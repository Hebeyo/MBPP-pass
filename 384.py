'''Write a python function to find the frequency of the smallest value in a given array.
'''
def frequency_Of_Smallest(n,arr):
    mn = arr[0]
    freq = 1
    for i in range(1,n):
        if (arr[i] < mn):
            mn = arr[i]
            freq = 1
        elif (arr[i] == mn):
            freq += 1
    return freq
'''
Standard answer: 
def frequency_Of_Smallest(n,arr): 
    mn = arr[0] 
    freq = 1
    for i in range(1,n): 
        if (arr[i] < mn): 
            mn = arr[i] 
            freq = 1
        elif (arr[i] == mn): 
            freq += 1
    return freq 
'''
assert frequency_Of_Smallest(5,[1,2,3,4,3]) == 1
assert frequency_Of_Smallest(7,[3,1,2,5,6,2,3]) == 1
assert frequency_Of_Smallest(7,[3,3,6,3,7,4,9]) == 3
