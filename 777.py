'''Write a python function to find the sum of non-repeated elements in a given array.
'''
def find_Sum(arr,n):
    arr.sort()
    sum = arr[0]
    for i in range(0,n-1):
        if (arr[i] != arr[i+1]):
            sum = sum + arr[i+1]  
    return sum
'''
Standard answer: 
def find_Sum(arr,n): 
    arr.sort() 
    sum = arr[0] 
    for i in range(0,n-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
'''
assert find_Sum([1,2,3,1,1,4,5,6],8) == 21
assert find_Sum([1,10,9,4,2,10,10,45,4],9) == 71
assert find_Sum([12,10,9,45,2,10,10,45,10],9) == 78
