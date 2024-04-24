'''Write a function to count repeated items of a tuple.
'''
def count_tuplex(tuplex,value):  
  count = 0
  for x in tuplex:
    if x == value:
      count += 1
  return count
'''
Standard answer: 
def count_tuplex(tuplex,value):  
  count = tuplex.count(value)
  return count
'''
assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),4)==3
assert count_tuplex((2, 4, 5, 6, 2, 3, 4, 4, 7),2)==2
assert count_tuplex((2, 4, 7, 7, 7, 3, 4, 4, 7),7)==4
