'''Write a function to extract unique values from the given dictionary values.
'''
def extract_unique(test_dict):
  res = []
  for val in test_dict.values():
    for ele in val:
      if ele not in res:
        res.append(ele)
  return list(sorted(res))
'''
Standard answer: 
def extract_unique(test_dict):
  res = list(sorted({ele for val in test_dict.values() for ele in val}))
  return res
'''
assert extract_unique({'msm' : [5, 6, 7, 8],'is' : [10, 11, 7, 5],'best' : [6, 12, 10, 8],'for' : [1, 2, 5]} ) == [1, 2, 5, 6, 7, 8, 10, 11, 12]
assert extract_unique({'Built' : [7, 1, 9, 4],'for' : [11, 21, 36, 14, 9],'ISP' : [4, 1, 21, 39, 47],'TV' : [1, 32, 38]} ) == [1, 4, 7, 9, 11, 14, 21, 32, 36, 38, 39, 47]
assert extract_unique({'F' : [11, 13, 14, 17],'A' : [12, 11, 15, 18],'N' : [19, 21, 15, 36],'G' : [37, 36, 35]}) == [11, 12, 13, 14, 15, 17, 18, 19, 21, 35, 36, 37]
