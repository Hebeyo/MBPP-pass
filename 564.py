'''Write a python function to count unequal element pairs from the given array.
'''
def count_Pairs(arr,n): 
    cnt = 0; 
    for i in range(n): 
        for j in range(i + 1,n): 
            if (arr[i] != arr[j]): 
                cnt += 1; 
    return cnt;
'''
Standard answer: 
def count_Pairs(arr,n): 
    cnt = 0; 
    for i in range(n): 
        for j in range(i + 1,n): 
            if (arr[i] != arr[j]): 
                cnt += 1; 
    return cnt; 
'''
assert count_Pairs([1,2,1],3) == 2
assert count_Pairs([1,1,1,1],4) == 0
assert count_Pairs([1,2,3,4,5],5) == 10
