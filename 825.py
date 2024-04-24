'''Write a python function to access multiple elements of specified index from a given list.
'''
def access_elements(nums, list_index):
    result = []
    for i in list_index:
        result.append(nums[i])
    return result
'''
Standard answer: 
def access_elements(nums, list_index):
    result = [nums[i] for i in list_index]
    return result
'''
assert access_elements([2,3,8,4,7,9],[0,3,5]) == [2, 4, 9]
assert access_elements([1, 2, 3, 4, 5],[1,2]) == [2,3]
assert access_elements([1,0,2,3],[0,1]) == [1,0]
