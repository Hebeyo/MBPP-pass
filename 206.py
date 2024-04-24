'''Write a function to perform the adjacent element concatenation in the given tuples.
'''
def concatenate_elements(test_tup):
  res = []
  for i in range(len(test_tup)-1):
    res.append(test_tup[i] + test_tup[i+1])
  return tuple(res)
'''
Standard answer: 
def concatenate_elements(test_tup):
  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 
'''
assert concatenate_elements(("DSP ", "IS ", "BEST ", "FOR ", "ALL ", "UTS")) == ('DSP IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL UTS')
assert concatenate_elements(("RES ", "IS ", "BEST ", "FOR ", "ALL ", "QESR")) == ('RES IS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL QESR')
assert concatenate_elements(("MSAM", "IS ", "BEST ", "FOR ", "ALL ", "SKD")) == ('MSAMIS ', 'IS BEST ', 'BEST FOR ', 'FOR ALL ', 'ALL SKD')
