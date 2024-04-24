'''Write a function to find numbers divisible by m and n from a list of numbers using lambda function.
'''
def div_of_nums(nums,m,n):
    result = []
    for i in nums:
        if i % m == 0 and i % n == 0:
            result.append(i)
    return result
'''
Standard answer: 
def div_of_nums(nums,m,n):
 result = list(filter(lambda x: (x % m == 0 and x % n == 0), nums)) 
 return result
'''
assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],2,4)==[ 152,44]
assert div_of_nums([1, 2, 3, 5, 7, 8, 10],2,5)==[10]
assert div_of_nums([10,15,14,13,18,12,20],10,5)==[10,20]
