'''Write a function to convert the given tuples into set.
'''
def tuple_to_set(t):
  s = set(t)
  return (s)
'''
Standard answer: 
def tuple_to_set(t):
  s = set(t)
  return (s) 
'''
assert tuple_to_set(('x', 'y', 'z') ) == {'y', 'x', 'z'}
assert tuple_to_set(('a', 'b', 'c') ) == {'c', 'a', 'b'}
assert tuple_to_set(('z', 'd', 'e') ) == {'d', 'e', 'z'}
