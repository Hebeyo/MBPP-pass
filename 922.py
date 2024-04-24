'''Write a function to find a pair with the highest product from a given array of integers.
'''
def max_product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return None     
    x = arr[0]; y = arr[1]    
    for i in range(0, arr_len): 
        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y
'''
Standard answer: 
def max_product(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return None     
    x = arr[0]; y = arr[1]    
    for i in range(0, arr_len): 
        for j in range(i + 1, arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y   
'''
assert max_product([1, 2, 3, 4, 7, 0, 8, 4])==(7, 8)
assert max_product([0, -1, -2, -4, 5, 0, -6])==(-4, -6)
assert max_product([1, 3, 5, 6, 8, 9])==(8,9)
