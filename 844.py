'''Write a python function to find the kth element in an array containing odd elements first and then even elements.
'''
def get_Number(n, k): 
    arr = [0] * n; 
    i = 0; 
    odd = 1; 
    while (odd <= n):   
        arr[i] = odd; 
        i += 1; 
        odd += 2;
    even = 2; 
    while (even <= n): 
        arr[i] = even; 
        i += 1;
        even += 2; 
    return arr[k - 1];
'''
Standard answer: 
def get_Number(n, k): 
    arr = [0] * n; 
    i = 0; 
    odd = 1; 
    while (odd <= n):   
        arr[i] = odd; 
        i += 1; 
        odd += 2;
    even = 2; 
    while (even <= n): 
        arr[i] = even; 
        i += 1;
        even += 2; 
    return arr[k - 1]; 
'''
assert get_Number(8,5) == 2
assert get_Number(7,2) == 3
assert get_Number(5,2) == 3
