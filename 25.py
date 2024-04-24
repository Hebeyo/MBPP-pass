'''Write a python function to find the product of non-repeated elements in a given array.
'''
def find_Product(arr,n):
    arr.sort()
    prod = 1
    for i in range(0,n,1):
        if (arr[i - 1] != arr[i]):
            prod = prod * arr[i]
    return prod
'''
Standard answer: 
def find_Product(arr,n): 
    arr.sort() 
    prod = 1
    for i in range(0,n,1): 
        if (arr[i - 1] != arr[i]): 
            prod = prod * arr[i] 
    return prod; 
'''
assert find_Product([1,1,2,3],4) == 6
assert find_Product([1,2,3,1,1],5) == 6
assert find_Product([1,1,4,5,6],5) == 120
assert find_Product([1,1,4,5,6,5,7,1,1,3,4],11) == 2520
