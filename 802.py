'''Write a python function to count the number of rotations required to generate a sorted array.
'''
def count_Rotation(arr,n):
    for i in range (1,n):
        if (arr[i] < arr[i - 1]):
            return i
    return 0
'''
Standard answer: 
def count_Rotation(arr,n):   
    for i in range (1,n): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
'''
assert count_Rotation([3,2,1],3) == 1
assert count_Rotation([4,5,1,2,3],5) == 2
assert count_Rotation([7,8,9,1,2,3],6) == 3
