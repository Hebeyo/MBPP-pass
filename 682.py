'''Write a function to multiply two lists using map and lambda function.
'''
def mul_list(nums1,nums2):
  result = map(lambda x, y: x * y, nums1, nums2)
  return list(result)
'''
Standard answer: 
def mul_list(nums1,nums2):
  result = map(lambda x, y: x * y, nums1, nums2)
  return list(result)
'''
assert mul_list([1, 2, 3],[4,5,6])==[4,10,18]
assert mul_list([1,2],[3,4])==[3,8]
assert mul_list([90,120],[50,70])==[4500,8400]
