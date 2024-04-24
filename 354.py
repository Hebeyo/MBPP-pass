'''Write a function to find t-nth term of arithemetic progression.
'''
def tn_ap(a,n,d):
  tn = a
  for i in range(1,n):
    tn += d
  return tn
'''
Standard answer: 
def tn_ap(a,n,d):
  tn = a + (n - 1) * d
  return tn
'''
assert tn_ap(1,5,2)==9
assert tn_ap(2,6,4)==22
assert tn_ap(1,4,5)==16
