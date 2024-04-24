'''Write a function to count the elements in a list until an element is a tuple.
'''
def count_elim(num):
  count_elim = 0
  for n in num:
    if isinstance(n, tuple):
        break
    count_elim += 1
  return count_elim
'''
Standard answer: 
def count_elim(num):
  count_elim = 0
  for n in num:
    if isinstance(n, tuple):
        break
    count_elim += 1
  return count_elim
'''
assert count_elim([10,20,30,(10,20),40])==3
assert count_elim([10,(20,30),(10,20),40])==1
assert count_elim([(10,(20,30,(10,20),40))])==0
