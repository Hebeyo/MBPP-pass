'''Write a python function to count the number of pairs whose sum is equal to ‘sum’.
'''
def get_Pairs_Count(arr,n,sum):
    count = 0  
    for i in range(0,n):
        for j in range(i + 1,n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
'''
Standard answer: 
def get_Pairs_Count(arr,n,sum):
    count = 0  
    for i in range(0,n):
        for j in range(i + 1,n):
            if arr[i] + arr[j] == sum:
                count += 1
    return count
'''
assert get_Pairs_Count([1,1,1,1],4,2) == 6
assert get_Pairs_Count([1,5,7,-1,5],5,6) == 3
assert get_Pairs_Count([1,-2,3],3,1) == 1
