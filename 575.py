'''Write a python function to find nth number in a sequence which is not a multiple of a given number.
'''
def count_no (A,N,L,R): 
    count = 0
    for i in range (L,R + 1): 
        if (i % A != 0): 
            count += 1
        if (count == N): 
            break
    return (i)
'''
Standard answer: 
def count_no (A,N,L,R): 
    count = 0
    for i in range (L,R + 1): 
        if (i % A != 0): 
            count += 1
        if (count == N): 
            break
    return (i) 
'''
assert count_no(2,3,1,10) == 5
assert count_no(3,6,4,20) == 11
assert count_no(5,10,4,20) == 16
