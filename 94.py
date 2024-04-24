'''Write a function to extract the index minimum value record from the given tuples.
'''
def index_minimum(test_list):
  res = min(test_list, key = lambda x: x[1])[0]
  return (res)
'''
Standard answer: 
from operator import itemgetter 
def index_minimum(test_list):
  res = min(test_list, key = itemgetter(1))[0]
  return (res) 
'''
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
assert index_minimum([('Yash', 185), ('Dawood', 125), ('Sanya', 175)]) == 'Dawood'
assert index_minimum([('Sai', 345), ('Salman', 145), ('Ayesha', 96)]) == 'Ayesha'
