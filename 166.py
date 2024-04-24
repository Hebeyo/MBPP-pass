'''Write a python function to count the pairs with xor as an even number.
'''
def find_even_Pair(A,N):
    evenPair = 0
    for i in range(0,N):
        for j in range(i+1,N):
            if ((A[i] ^ A[j]) % 2 == 0):
                evenPair+=1
    return evenPair
'''
Standard answer: 
def find_even_Pair(A,N): 
    evenPair = 0
    for i in range(0,N): 
        for j in range(i+1,N): 
            if ((A[i] ^ A[j]) % 2 == 0): 
                evenPair+=1
    return evenPair; 
'''
assert find_even_Pair([5,4,7,2,1],5) == 4
assert find_even_Pair([7,2,8,1,0,5,11],7) == 9
assert find_even_Pair([1,2,3],3) == 1
