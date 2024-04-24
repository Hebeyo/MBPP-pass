'''Write a function to print the first n lucky numbers.
'''
def lucky_num(n):
 List=range(-1,n*n+9,2)
 i=2
 while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
 return List[1:n+1]
'''
Standard answer: 
def lucky_num(n):
 List=range(-1,n*n+9,2)
 i=2
 while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
 return List[1:n+1]
'''
assert lucky_num(10)==[1, 3, 7, 9, 13, 15, 21, 25, 31, 33] 
assert lucky_num(5)==[1, 3, 7, 9, 13]
assert lucky_num(8)==[1, 3, 7, 9, 13, 15, 21, 25]
