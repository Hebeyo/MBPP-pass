'''Write a python function to count number of substrings with the sum of digits equal to their length.
'''
def count_Substrings(s,n):
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += int(s[j])
            if sum == j - i + 1:
                count += 1
    return count
'''
Standard answer: 
from collections import defaultdict
def count_Substrings(s,n):
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
'''
assert count_Substrings('112112',6) == 6
assert count_Substrings('111',3) == 6
assert count_Substrings('1101112',7) == 12
