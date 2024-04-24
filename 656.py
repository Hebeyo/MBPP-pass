'''Write a python function to find the minimum sum of absolute differences of two arrays.
'''
def find_Min_Sum(a,b,n):
    a.sort()
    b.sort()
    sum = 0
    for i in range(n):
        sum = sum + abs(a[i] - b[i])
    return sum
'''
Standard answer: 
def find_Min_Sum(a,b,n): 
    a.sort() 
    b.sort() 
    sum = 0  
    for i in range(n): 
        sum = sum + abs(a[i] - b[i]) 
    return sum
'''
assert find_Min_Sum([3,2,1],[2,1,3],3) == 0
assert find_Min_Sum([1,2,3],[4,5,6],3) == 9
assert find_Min_Sum([4,1,8,7],[2,3,6,5],4) == 6
