'''Write a python function to find the sum of repeated elements in a given array.
'''
def find_Sum(arr,n):
    sum = 0
    for i in range(0,n,1):
        if (arr.count(arr[i]) > 1):
            sum = sum + arr[i]
    return sum
'''
Standard answer: 
def find_Sum(arr,n): 
    return sum([x for x in arr if arr.count(x) > 1])
'''
assert find_Sum([1,2,3,1,1,4,5,6],8) == 3
assert find_Sum([1,2,3,1,1],5) == 3
assert find_Sum([1,1,2],3) == 2
assert find_Sum([1,1,2,3,4,5,6,3,5],9) == 18
