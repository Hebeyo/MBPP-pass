'''Write a function to increment the numeric values in the given strings by k.
'''
def increment_numerics(test_list, K):
  res = []
  for ele in test_list:
    if ele.isdigit():
      res.append(str(int(ele) + K))
    else:
      res.append(ele)
  return res
'''
Standard answer: 
def increment_numerics(test_list, K):
  res = [str(int(ele) + K) if ele.isdigit() else ele for ele in test_list]
  return res 
'''
assert increment_numerics(["MSM", "234", "is", "98", "123", "best", "4"] , 6) == ['MSM', '240', 'is', '104', '129', 'best', '10']
assert increment_numerics(["Dart", "356", "is", "88", "169", "Super", "6"] , 12) == ['Dart', '368', 'is', '100', '181', 'Super', '18']
assert increment_numerics(["Flutter", "451", "is", "44", "96", "Magnificent", "12"] , 33) == ['Flutter', '484', 'is', '77', '129', 'Magnificent', '45']
