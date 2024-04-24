'''Write a python function to find number of integers with odd number of set bits.
'''
def count_With_Odd_SetBits(n):
    count = 0
    for i in range(1,n+1):
        if bin(i).count('1') % 2 != 0:
            count += 1
    return count
'''
Standard answer: 
def count_With_Odd_SetBits(n): 
    if (n % 2 != 0): 
        return (n + 1) / 2
    count = bin(n).count('1') 
    ans = n / 2
    if (count % 2 != 0): 
        ans += 1
    return ans 
'''
assert count_With_Odd_SetBits(5) == 3
assert count_With_Odd_SetBits(10) == 5
assert count_With_Odd_SetBits(15) == 8
