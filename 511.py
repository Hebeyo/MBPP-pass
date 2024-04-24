'''Write a python function to find minimum sum of factors of a given number.
'''
def find_Min_Sum(num):
    sum = 0
    i = 2
    while i * i <= num:
        while num % i == 0:
            sum += i
            num /= i
        i += 1
    sum += num
    return sum
'''
Standard answer: 
def find_Min_Sum(num): 
    sum = 0
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num 
    return sum
'''
assert find_Min_Sum(12) == 7
assert find_Min_Sum(105) == 15
assert find_Min_Sum(2) == 2
