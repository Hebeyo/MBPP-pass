'''Write a function to add two lists using map and lambda function.
'''
def add_list(nums1,nums2):
  result = map(lambda x, y: x + y, nums1, nums2)
  return list(result)
'''
Standard answer: 
def add_list(nums1,nums2):
  result = map(lambda x, y: x + y, nums1, nums2)
  return list(result)
'''
assert add_list([1, 2, 3],[4,5,6])==[5, 7, 9]
assert add_list([1,2],[3,4])==[4,6]
assert add_list([10,20],[50,70])==[60,90]
