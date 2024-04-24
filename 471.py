'''Write a python function to find remainder of array multiplication divided by n.
'''
def find_remainder(arr, lens, n): 
    mul = 1
    for i in range(lens):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n
'''
Standard answer: 
def find_remainder(arr, lens, n): 
    mul = 1
    for i in range(lens):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 
'''
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],6,11) ==9
assert find_remainder([1,1,1],3,1) == 0
assert find_remainder([1,2,1],3,2) == 0
