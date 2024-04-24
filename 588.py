'''Write a python function to find the difference between largest and smallest value in a given array.
'''
def big_diff(nums):
    max_num = nums[0]
    min_num = nums[0]
    for num in nums:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
    return max_num - min_num
'''
Standard answer: 
def big_diff(nums):
     diff= max(nums)-min(nums)
     return diff
'''
assert big_diff([1,2,3,4]) == 3
assert big_diff([4,5,12]) == 8
assert big_diff([9,2,3]) == 7
