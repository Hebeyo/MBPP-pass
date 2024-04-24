'''Write a function to find m number of multiples of n.
'''
def multiples_of_num(m,n):
    result=[]
    for i in range(1,m+1):
        result.append(n*i)
    return result
'''
Standard answer: 
def multiples_of_num(m,n): 
    multiples_of_num= list(range(n,(m+1)*n, n)) 
    return list(multiples_of_num)
'''
assert multiples_of_num(4,3)== [3,6,9,12]
assert multiples_of_num(2,5)== [5,10]
assert multiples_of_num(9,2)== [2,4,6,8,10,12,14,16,18]
