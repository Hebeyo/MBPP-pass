'''Write a python function to find the minimum element in a sorted and rotated array.
'''
def find_Min(arr,low,high):
    while (low < high):
        mid = low + (high - low) // 2
        if (arr[mid] == arr[high]):
            high -= 1
        elif (arr[mid] > arr[high]):
            low = mid + 1
        else:
            high = mid
    return arr[high]
'''
Standard answer: 
def find_Min(arr,low,high): 
    while (low < high): 
        mid = low + (high - low) // 2;   
        if (arr[mid] == arr[high]): 
            high -= 1; 
        elif (arr[mid] > arr[high]): 
            low = mid + 1; 
        else: 
            high = mid; 
    return arr[high]; 
'''
assert find_Min([1,2,3,4,5],0,4) == 1
assert find_Min([4,6,8],0,2) == 4
assert find_Min([2,3,5,7,9],0,4) == 2
