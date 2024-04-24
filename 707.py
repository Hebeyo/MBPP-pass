'''Write a python function to count the total set bits from 1 to n.
'''
def count_Set_Bits(n) :  
    cnt = 0
    for i in range(1, n + 1) : 
        cnt += bin(i).count('1')
    return cnt
'''
Standard answer: 
def count_Set_Bits(n) :  
    n += 1; 
    powerOf2 = 2;   
    cnt = n // 2;  
    while (powerOf2 <= n) : 
        totalPairs = n // powerOf2;  
        cnt += (totalPairs // 2) * powerOf2;  
        if (totalPairs & 1) : 
            cnt += (n % powerOf2) 
        else : 
            cnt += 0
        powerOf2 <<= 1;    
    return cnt;  
'''
assert count_Set_Bits(16) == 33
assert count_Set_Bits(2) == 2
assert count_Set_Bits(14) == 28
