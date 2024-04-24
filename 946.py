'''Write a function to find the most common elements and their counts of a specified text.
'''
def most_common_elem(s,a):
  from collections import Counter
  most_common_elem=Counter(s).most_common(a)
  return most_common_elem
'''
Standard answer: 
from collections import Counter 
def most_common_elem(s,a):
  most_common_elem=Counter(s).most_common(a)
  return most_common_elem
'''
assert most_common_elem('lkseropewdssafsdfafkpwe',3)==[('s', 4), ('e', 3), ('f', 3)] 
assert most_common_elem('lkseropewdssafsdfafkpwe',2)==[('s', 4), ('e', 3)]
assert most_common_elem('lkseropewdssafsdfafkpwe',7)==[('s', 4), ('e', 3), ('f', 3), ('k', 2), ('p', 2), ('w', 2), ('d', 2)]
