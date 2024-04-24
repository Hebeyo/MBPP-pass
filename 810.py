'''Write a function to iterate over elements repeating each as many times as its count.
'''
def count_variable(a,b,c,d):
    return ['p']*a + ['q']*b + ['r']*c + ['s']*d
'''
Standard answer: 
from collections import Counter
def count_variable(a,b,c,d):
  c = Counter(p=a, q=b, r=c, s=d)
  return list(c.elements())
'''
assert count_variable(4,2,0,-2)==['p', 'p', 'p', 'p', 'q', 'q'] 
assert count_variable(0,1,2,3)==['q', 'r', 'r', 's', 's', 's'] 
assert count_variable(11,15,12,23)==['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's']
