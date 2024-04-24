'''Write a python function to check whether a sequence of numbers has an increasing trend or not.
'''
def increasing_trend(nums):
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            return False
    return True
'''
Standard answer: 
def increasing_trend(nums):
    if (sorted(nums)== nums):
        return True
    else:
        return False
'''
assert increasing_trend([1,2,3,4]) == True
assert increasing_trend([4,3,2,1]) == False
assert increasing_trend([0,1,4,9]) == True
