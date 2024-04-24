'''Write a python function to calculate the sum of the numbers in a list between the indices of a specified range.
'''
def sum_Range_list(nums, m, n):
    sum_range = 0
    for i in range(m, n+1, 1):
        sum_range += nums[i]
    return sum_range
'''
Standard answer: 
def sum_Range_list(nums, m, n):                                                                                                                                                                                                
    sum_range = 0                                                                                                                                                                                                         
    for i in range(m, n+1, 1):                                                                                                                                                                                        
        sum_range += nums[i]                                                                                                                                                                                                  
    return sum_range   
'''
assert sum_Range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12],8,10) == 29
assert sum_Range_list([1,2,3,4,5],1,2) == 5
assert sum_Range_list([1,0,1,2,5,6],4,5) == 11
