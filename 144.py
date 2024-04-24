'''Write a python function to find the sum of absolute differences in all pairs of the given array.
'''
def sum_Pairs(arr,n):
    sum = 0
    for i in range(n - 1,-1,-1):
        sum += i*arr[i] - (n-1-i) * arr[i]
    return sum
'''
Standard answer: 
def sum_Pairs(arr,n): 
    sum = 0
    for i in range(n - 1,-1,-1): 
        sum += i*arr[i] - (n-1-i) * arr[i] 
    return sum
'''
assert sum_Pairs([1,8,9,15,16],5) == 74
assert sum_Pairs([1,2,3,4],4) == 10
assert sum_Pairs([1,2,3,4,5,7,9,11,14],9) == 188
