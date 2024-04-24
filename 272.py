'''Write a function to perfom the rear element extraction from list of tuples records.
'''
def rear_extract(test_list):
  res = [lis[-1] for lis in test_list]
  return (res)
'''
Standard answer: 
def rear_extract(test_list):
  res = [lis[-1] for lis in test_list]
  return (res) 
'''
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
assert rear_extract([(1, 'Sai', 36), (2, 'Ayesha', 25), (3, 'Salman', 45)]) == [36, 25, 45]
assert rear_extract([(1, 'Sudeep', 14), (2, 'Vandana', 36), (3, 'Dawood', 56)]) == [14, 36, 56]
