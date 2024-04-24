'''Write a function to solve gold mine problem.
'''
def get_maxgold(gold, m, n): 
    goldTable = [[0 for i in range(n)] 
                        for j in range(m)]   
    for col in range(n-1, -1, -1): 
        for row in range(m):  
            if (col == n-1): 
                right = 0
            else: 
                right = goldTable[row][col+1] 
            if (row == 0 or col == n-1): 
                right_up = 0
            else: 
                right_up = goldTable[row-1][col+1] 
            if (row == m-1 or col == n-1): 
                right_down = 0
            else: 
                right_down = goldTable[row+1][col+1] 
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down) 
    res = goldTable[0][0] 
    for i in range(1, m): 
        res = max(res, goldTable[i][0])  
    return res
'''
Standard answer: 
def get_maxgold(gold, m, n): 
    goldTable = [[0 for i in range(n)] 
                        for j in range(m)]   
    for col in range(n-1, -1, -1): 
        for row in range(m):  
            if (col == n-1): 
                right = 0
            else: 
                right = goldTable[row][col+1] 
            if (row == 0 or col == n-1): 
                right_up = 0
            else: 
                right_up = goldTable[row-1][col+1] 
            if (row == m-1 or col == n-1): 
                right_down = 0
            else: 
                right_down = goldTable[row+1][col+1] 
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down) 
    res = goldTable[0][0] 
    for i in range(1, m): 
        res = max(res, goldTable[i][0])  
    return res 
'''
assert get_maxgold([[1, 3, 1, 5],[2, 2, 4, 1],[5, 0, 2, 3],[0, 6, 1, 2]],4,4)==16
assert get_maxgold([[10,20],[30,40]],2,2)==70
assert get_maxgold([[4,9],[3,7]],2,2)==13
