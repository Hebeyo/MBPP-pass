'''Write a function to check if the given array represents min heap or not.
'''
def check_min_heap(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap(arr, 2 * i + 2))
    return left_child and right_child
'''
Standard answer: 
def check_min_heap(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap(arr, 2 * i + 2))
    return left_child and right_child
'''
assert check_min_heap([1, 2, 3, 4, 5, 6], 0) == True
assert check_min_heap([2, 3, 4, 5, 10, 15], 0) == True
assert check_min_heap([2, 10, 4, 5, 3, 15], 0) == False
