'''Write a function to add two integers. however, if the sum is between the given range it will return 20.
'''
def sum_nums(x, y,m,n):
    sum_nums= x + y
    if sum_nums in range(m, n):
        return 20
    else:
        return sum_nums
'''
Standard answer: 
def sum_nums(x, y,m,n):
    sum_nums= x + y
    if sum_nums in range(m, n):
        return 20
    else:
        return sum_nums
'''
assert sum_nums(2,10,11,20)==20
assert sum_nums(15,17,1,10)==32
assert sum_nums(10,15,5,30)==20
