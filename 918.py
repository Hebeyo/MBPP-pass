'''Write a function to count coin change.
'''
def coin_change(S, m, n): 
    table = [[0 for x in range(m)] for x in range(n+1)] 
    for i in range(m): 
        table[0][i] = 1
    for i in range(1, n+1): 
        for j in range(m): 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0 
            table[i][j] = x + y   
    return table[n][m-1]
'''
Standard answer: 
def coin_change(S, m, n): 
    table = [[0 for x in range(m)] for x in range(n+1)] 
    for i in range(m): 
        table[0][i] = 1
    for i in range(1, n+1): 
        for j in range(m): 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0 
            table[i][j] = x + y   
    return table[n][m-1] 
'''
assert coin_change([1, 2, 3],3,4)==4
assert coin_change([4,5,6,7,8,9],6,9)==2
assert coin_change([4,5,6,7,8,9],6,4)==1
