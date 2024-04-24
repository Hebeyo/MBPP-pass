'''Write a python function to check whether the product of numbers is even or not.
'''
def is_Product_Even(arr,n):
    product = 1
    for i in range(n):
        product *= arr[i]
    if product % 2 == 0:
        return True
    else:
        return False
'''
Standard answer: 
def is_Product_Even(arr,n): 
    for i in range(0,n): 
        if ((arr[i] & 1) == 0): 
            return True
    return False
'''
assert is_Product_Even([1,2,3],3) == True
assert is_Product_Even([1,2,1,4],4) == True
assert is_Product_Even([1,1],2) == False
