'''Write a function to find numbers divisible by m or n from a list of numbers using lambda function.
'''
def div_of_nums(nums,m,n):
 result = list(filter(lambda x: (x % m == 0 or x % n == 0), nums)) 
 return result
'''
Standard answer: 
def div_of_nums(nums,m,n):
 result = list(filter(lambda x: (x % m == 0 or x % n == 0), nums)) 
 return result
'''
assert div_of_nums([19, 65, 57, 39, 152, 639, 121, 44, 90, 190],19,13)==[19, 65, 57, 39, 152, 190]
assert div_of_nums([1, 2, 3, 5, 7, 8, 10],2,5)==[2, 5, 8, 10]
assert div_of_nums([10,15,14,13,18,12,20],10,5)==[10, 15, 20]
