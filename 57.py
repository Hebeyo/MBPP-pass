'''Write a python function to find the largest number that can be formed with the given digits.
'''
def find_Max_Num(arr,n):
    arr.sort(reverse = True)
    num = arr[0]
    for i in range(1,n):
        num = num * 10 + arr[i]
    return num
'''
Standard answer: 
def find_Max_Num(arr,n) : 
    arr.sort(reverse = True) 
    num = arr[0] 
    for i in range(1,n) : 
        num = num * 10 + arr[i] 
    return num 
'''
assert find_Max_Num([1,2,3],3) == 321
assert find_Max_Num([4,5,6,1],4) == 6541
assert find_Max_Num([1,2,3,9],4) == 9321
