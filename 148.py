'''Write a function to divide a number into two parts such that the sum of digits is maximum.
'''
def sum_digits_twoparts(N):
    def sum_digits_single(x) : 
        ans = 0
        while x : 
            ans += x % 10
            x //= 10  
        return ans 
    def closest(x) : 
        ans = 0
        while (ans * 10 + 9 <= x) : 
            ans = ans * 10 + 9  
        return ans   
    A = closest(N)  
    return sum_digits_single(A) + sum_digits_single(N - A)
'''
Standard answer: 
def sum_digits_single(x) : 
    ans = 0
    while x : 
        ans += x % 10
        x //= 10  
    return ans 
def closest(x) : 
    ans = 0
    while (ans * 10 + 9 <= x) : 
        ans = ans * 10 + 9  
    return ans   
def sum_digits_twoparts(N) : 
    A = closest(N)  
    return sum_digits_single(A) + sum_digits_single(N - A) 
'''
assert sum_digits_twoparts(35)==17
assert sum_digits_twoparts(7)==7
assert sum_digits_twoparts(100)==19
