'''Write a function to remove an empty tuple from a list of tuples.
'''
def remove_empty(tuple1): #L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
   tuple1 = [t for t in tuple1 if t]
   return tuple1
'''
Standard answer: 
def remove_empty(tuple1): #L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
   tuple1 = [t for t in tuple1 if t]
   return tuple1
'''
assert remove_empty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])==[('',), ('a', 'b'), ('a', 'b', 'c'), 'd']  
assert remove_empty([(), (), ('',), ("python"), ("program")])==[('',), ("python"), ("program")]  
assert remove_empty([(), (), ('',), ("java")])==[('',),("java") ]  
