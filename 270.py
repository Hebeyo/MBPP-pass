'''Write a python function to find the sum of even numbers at even positions.
'''
def sum_even_and_even_index(arr,n):
    sum = 0
    for i in range(0,n,2):
        if (arr[i] % 2 == 0):
            sum += arr[i]
    return sum
'''
Standard answer: 
def sum_even_and_even_index(arr,n):  
    i = 0
    sum = 0
    for i in range(0,n,2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
'''
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8],6) == 30
assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18],10) == 26
assert sum_even_and_even_index([5, 6, 12, 1],4) == 12
