'''Write a function to extract specified number of elements from a given list, which follow each other continuously.
'''
def extract_elements(numbers, n):
    result = []
    for i in range(len(numbers)-n+1):
        if numbers[i:i+n] == [numbers[i]]*n:
            result.append(numbers[i])
    return result
'''
Standard answer: 
from itertools import groupby 
def extract_elements(numbers, n):
    result = [i for i, j in groupby(numbers) if len(list(j)) == n] 
    return result
'''
assert extract_elements([1, 1, 3, 4, 4, 5, 6, 7],2)==[1, 4]
assert extract_elements([0, 1, 2, 3, 4, 4, 4, 4, 5, 7],4)==[4]
assert extract_elements([0,0,0,0,0],5)==[0]
