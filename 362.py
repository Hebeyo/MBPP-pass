'''Write a python function to find the item with maximum occurrences in a given list.
'''
def max_occurrences(nums):
    max_val = 0
    result = nums[0] 
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result
'''
Standard answer: 
def max_occurrences(nums):
    max_val = 0
    result = nums[0] 
    for i in nums:
        occu = nums.count(i)
        if occu > max_val:
            max_val = occu
            result = i 
    return result
'''
assert max_occurrences([1,2,3,1,2,3,12,4,2]) ==  2
assert max_occurrences([1,2,6,7,0,1,0,1,0]) == 1,0
assert max_occurrences([1,2,3,1,2,4,1]) == 1
