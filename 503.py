'''Write a function to add consecutive numbers of a given list.
'''
def add_consecutive_nums(nums):
    result = []
    for i in range(len(nums)-1):
        result.append(nums[i]+nums[i+1])
    return result
'''
Standard answer: 
def add_consecutive_nums(nums):
    result = [b+a for a, b in zip(nums[:-1], nums[1:])]
    return result
'''
assert add_consecutive_nums([1, 1, 3, 4, 4, 5, 6, 7])==[2, 4, 7, 8, 9, 11, 13]
assert add_consecutive_nums([4, 5, 8, 9, 6, 10])==[9, 13, 17, 15, 16]
assert add_consecutive_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[3, 5, 7, 9, 11, 13, 15, 17, 19]
