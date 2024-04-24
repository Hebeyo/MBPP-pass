'''Write a python function to find sum of inverse of divisors.
'''
def Sum_of_Inverse_Divisors(N,Sum): 
    ans = float(Sum)*1.0 /float(N);  
    return round(ans,2);
'''
Standard answer: 
def Sum_of_Inverse_Divisors(N,Sum): 
    ans = float(Sum)*1.0 /float(N);  
    return round(ans,2); 
'''
assert Sum_of_Inverse_Divisors(6,12) == 2
assert Sum_of_Inverse_Divisors(9,13) == 1.44
assert Sum_of_Inverse_Divisors(1,4) == 4
